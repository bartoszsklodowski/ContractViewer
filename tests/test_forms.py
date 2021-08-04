import pytest
import pytz
from datetime import date, timedelta, datetime
from accounts.forms import CustomEmailValidationOnForgotPassword
from contracts.forms import AddressModelForm, CustomerModelForm, RegionModelForm, PersonalDataModelForm
from contracts.forms import DepartmentModelForm, EmployeeModelForm, ContractModelForm, BuildingModelForm
from contracts.forms import DrawingModelForm
from django.contrib.auth import get_user_model


# ACCOUNTS

@pytest.mark.django_db
def test_custom_email_validation_valid_email(new_user):
    form = CustomEmailValidationOnForgotPassword(data={'email': new_user.email})
    user_model = get_user_model()
    assert user_model.objects.count() == 1
    assert form.is_valid()


@pytest.mark.django_db
def test_custom_email_validation_invalid_email(new_user):
    form = CustomEmailValidationOnForgotPassword(data={'email': 'example@example.com'})
    user_model = get_user_model()
    # group_ids = new_user.groups.filter(name='Staff').values_list('id', flat=True)
    # print(Permission.objects.filter(group__id__in=group_ids))
    assert user_model.objects.count() == 1
    assert not form.is_valid()
    assert len(form.errors) == 1
    assert "That email address doesn't have an associated user account. Are you sure you've registered?" == \
           form.errors['email'][0]


# CONTRACTS

def test_address_model_form_valid(db):
    form = AddressModelForm(data={'street': 'Sienkiewicza', 'zip_code': '05-200', 'town': 'Wolomin'})
    assert form.is_valid()


def test_address_model_form_invalid(db, address_factory):
    address = address_factory.create()
    form = AddressModelForm(data={'street': address.street, 'zip_code': address.zip_code, 'town': address.town})
    assert not form.is_valid()


def test_customer_model_form_valid(db, address_factory):
    address = address_factory.create()
    form = CustomerModelForm(data={'name': 'Kobi', 'description': '', 'address': address})
    assert form.is_valid()


def test_customer_model_form_invalid(db, customer_factory):
    customer = customer_factory.create()
    form = CustomerModelForm(
        data={'name': customer.name, 'description': customer.description, 'address': customer.address})
    assert not form.is_valid()


def test_region_model_form_valid(db, address_factory):
    address = address_factory.create()
    form = RegionModelForm(data={'name': 'Kobi', 'prefix': 286, 'address': address})
    assert form.is_valid()


def test_region_model_form_invalid(db, region_factory):
    region = region_factory.create()
    form = RegionModelForm(data={'name': region.name, 'prefix': region.prefix, 'address': region.address})
    assert not form.is_valid()


def test_personal_data_model_form_valid(db, address_factory):
    address = address_factory.create()
    form = PersonalDataModelForm(data={'name': 'Kobi', 'last_name': 'Kobi', 'address': address})
    assert form.is_valid()


def test_personal_data_model_form_invalid(db, personal_data_factory):
    personal_data = personal_data_factory.create()
    form = PersonalDataModelForm(
        data={'name': personal_data.name, 'last_name': personal_data.last_name, 'address': personal_data.address})
    assert not form.is_valid()


def test_department_model_form_valid(db):
    form = DepartmentModelForm(data={'name': 'Kobi', 'description': 'Kobi'})
    assert form.is_valid()


def test_department_model_form_invalid(db, department_factory):
    department = department_factory.create()
    form = DepartmentModelForm(data={'name': department.name, 'description': department.description})
    assert not form.is_valid()


def test_employee_model_form_valid(db, department_factory, personal_data_factory):
    department = department_factory.create()
    personal_data = personal_data_factory.create()
    form = EmployeeModelForm(data={'position': 'Technician', 'hire_date': '2020-01-01', 'personal_data': personal_data,
                                   'department': department})
    assert form.is_valid()


def test_employee_model_form_invalid_personal_data(db, employee_factory, department_factory, personal_data_factory):
    employee = employee_factory.create()
    department = department_factory.create()
    form = EmployeeModelForm(
        data={'position': employee.position, 'hire_date': employee.hire_date, 'personal_data': employee.personal_data,
              'department': department})
    assert not form.is_valid()


def test_employee_model_form_invalid_hire_date(db, employee_factory, department_factory, personal_data_factory):
    today_date = date.today()
    employee = employee_factory.create()
    department = department_factory.create()
    personal_data = personal_data_factory.create()
    form = EmployeeModelForm(
        data={'position': employee.position, 'hire_date': today_date + timedelta(1), 'personal_data': personal_data,
              'department': department})
    assert not form.is_valid()


def test_contract_model_form_valid(db, address_factory, customer_factory, region_factory):
    address = address_factory.create()
    customer = customer_factory.create()
    region = region_factory.create()
    form = ContractModelForm(data={'number': 5363, 'name': 'Road', 'type': 'abutment', 'start_date': '2020-01-01',
                                   'end_date': '2020-01-02', 'description': '', 'address': address,
                                   'customer': customer, 'region': region})
    assert form.is_valid()


def test_contract_model_form_invalid_exists(db, contract_factory):
    contract = contract_factory.create()
    form = ContractModelForm(data={'number': contract.number, 'name': contract.name, 'type': contract.type,
                                   'start_date': contract.start_date,
                                   'end_date': contract.end_date, 'description': contract.description,
                                   'address': contract.address,
                                   'customer': contract.customer, 'region': contract.region})
    assert not form.is_valid()


def test_contract_model_form_invalid_end_date(db, contract_factory):
    today_date = date.today()
    contract = contract_factory.create()
    form = ContractModelForm(data={'number': 5363, 'name': 'Road', 'type': 'abutment',
                                   'start_date': contract.start_date,
                                   'end_date': today_date + timedelta(1), 'description': contract.description,
                                   'address': contract.address,
                                   'customer': contract.customer, 'region': contract.region})
    assert not form.is_valid()


def test_contract_model_form_invalid_start_date(db, contract_factory):
    today_date = date.today()
    contract = contract_factory.create()
    form = ContractModelForm(data={'number': 5363, 'name': 'Road', 'type': 'abutment',
                                   'start_date': today_date + timedelta(1),
                                   'end_date': contract.end_date, 'description': contract.description,
                                   'address': contract.address,
                                   'customer': contract.customer, 'region': contract.region})
    assert not form.is_valid()


def test_building_model_form_valid(db, contract_factory):
    contract = contract_factory.create()
    form = BuildingModelForm(data={'name': 'Road', 'description': 'abutment', 'contract': contract})
    assert form.is_valid()


def test_building_model_form_invalid(db, building_factory):
    building = building_factory.create()
    form = BuildingModelForm(
        data={'name': building.name, 'description': building.description, 'contract': building.contract})
    assert not form.is_valid()


def test_drawing_model_form_valid(db, employee_factory, building_factory, contract_factory):
    technician = employee_factory.create()
    building = building_factory.create()
    contract = contract_factory.create()
    form = DrawingModelForm(
        data={'number': 1210, 'element': 'abutment', 'revision': 'a', 'creation_date': '2020-01-01 13:55:24',
              'modification_date': '2020-01-02 13:55:24', 'technician': technician,
              'building': building, 'contract': contract})
    assert form.is_valid()


def test_drawing_model_form_invalid_exists(db, drawing_factory):
    drawing = drawing_factory.create()
    form = DrawingModelForm(
        data={'number': drawing.number, 'element': 'abutment', 'revision': 'a', 'creation_date': '2020-01-01 13:55:24',
              'modification_date': '2020-01-02 13:55:24', 'technician': drawing.technician,
              'building': drawing.building, 'contract': drawing.contract})
    assert not form.is_valid()


def test_drawing_model_form_invalid_modification_date(db, drawing_factory, building_factory):
    utc = pytz.utc
    drawing = drawing_factory.create()
    building = building_factory.create()
    form = DrawingModelForm(
        data={'number': 1210, 'element': 'abutment', 'revision': 'a', 'creation_date': '2020-01-01 13:55:24',
              'modification_date': datetime.today().replace(tzinfo=utc) - timedelta(1),
              'technician': drawing.technician,
              'building': building, 'contract': drawing.contract})
    assert not form.is_valid()