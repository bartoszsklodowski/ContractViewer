from django.forms import CharField, Form, DateTimeField, ModelChoiceField, TextInput, ModelForm, IntegerField
from django.forms import ModelMultipleChoiceField, CheckboxSelectMultiple, SelectDateWidget
from contracts.models import Address, Customer, Region, PersonalData, Department, Employee, Contract, Building, Drawing
from django.core.exceptions import ValidationError
from datetime import datetime, date
import pytz


class AddressModelForm(ModelForm):
    class Meta:
        model = Address
        fields = "__all__"

    def clean(self):
        result = super().clean()
        for address in Address.objects.all():
            if result["street"].lower() == address.street.lower():
                raise ValidationError("Address is already exist")
        return result


class CustomerModelForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

    def clean(self):
        result = super().clean()
        for customer in Customer.objects.all():
            if result["name"].lower() == customer.name.lower():
                raise ValidationError("Customer is already exist")
        return result


class RegionModelForm(ModelForm):
    class Meta:
        model = Region
        fields = "__all__"

    def clean(self):
        result = super().clean()
        for region in Region.objects.all():
            if result["name"].lower() == region.name.lower() or result["prefix"] == region.prefix:
                raise ValidationError("Region is already exist")
        return result


class PersonalDataModelForm(ModelForm):
    class Meta:
        model = PersonalData
        fields = "__all__"

    def clean(self):
        result = super().clean()
        for data in PersonalData.objects.all():
            if result["name"].lower() == data.name.lower() and result["last_name"].lower() == data.last_name.lower():
                raise ValidationError("PersonalData is already exist")
        return result


class DepartmentModelForm(ModelForm):
    class Meta:
        model = Department
        fields = "__all__"

    def clean(self):
        result = super().clean()
        for department in Department.objects.all():
            if result["name"].lower() == department.name.lower():
                raise ValidationError("Department is already exist")
        return result


class EmployeeModelForm(ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {"hire_date": SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),
                                                 years=range(1990, 2030))}

    def clean(self):
        today_date = date.today()
        result = super().clean()
        for employee in Employee.objects.all():
            if result["personal_data"] == employee.personal_data:
                raise ValidationError("Employee with this personal data is already exist")
            if result["hire_date"] >= today_date:
                raise ValidationError("You can't assign hire date before today date")
        return result


class ContractModelForm(ModelForm):
    class Meta:
        model = Contract
        fields = "__all__"
        widgets = {"employee": CheckboxSelectMultiple,
                   "start_date": SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),
                                                  years=range(1990, 2030)),
                   "end_date": SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),
                                                years=range(1990, 2030))}

    def clean(self):
        today_date = date.today()
        result = super().clean()
        for contract in Contract.objects.all():
            if result["name"].lower() == contract.name.lower():
                raise ValidationError("Contract with this name is already exist")
            if result["number"] == contract.number:
                raise ValidationError("Contract with this number is already exist")
            if result["end_date"]:
                if result["end_date"] <= result["start_date"] or result["end_date"] >= today_date:
                    raise ValidationError("You can't assign end date before start date")
            if result["start_date"] >= today_date:
                raise ValidationError("You can't assign date before today date")
        return result


class BuildingModelForm(ModelForm):
    class Meta:
        model = Building
        fields = "__all__"

    def clean(self):
        result = super().clean()
        for building in Building.objects.all():
            if result["name"].lower() == building.name.lower():
                raise ValidationError("Building is already exist")
        return result


class DrawingModelForm(ModelForm):
    class Meta:
        model = Drawing
        fields = "__all__"
        widgets = {"modification_date": SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),
                                                         years=range(1990, 2030))}

    def clean(self):
        utc = pytz.utc
        result = super().clean()
        for drawing in Drawing.objects.all():
            if result["number"] == drawing.number and result["building"] == drawing.building:
                raise ValidationError("Drawing with this number is already exist")
            if result["modification_date"]:
                if datetime.strptime(datetime.strftime(result["modification_date"], '%Y-%m-%d %H:%M:%S'),
                        '%Y-%m-%d %H:%M:%S').replace(tzinfo=utc) <= datetime.today().replace(tzinfo=utc):
                    raise ValidationError("You can't assign modification date before creation date")
        return result
