import factory
from django.contrib.auth.models import User, Group, Permission
from faker import Faker
from contracts.models import Address, Customer, Region, PersonalData, Department, Employee, Contract, Building, Drawing
import pytz

fake = Faker()


class StaffGroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Group

    name = "Staff"


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.first_name()
    password = fake.password()
    email = fake.email()
    is_staff = 'True'


class SuperUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.first_name()
    password = fake.password()
    email = fake.email()
    is_superuser = 'True'


class AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Address

    street = fake.street_address()
    zip_code = fake.postcode()
    town = fake.city()


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    name = fake.name()
    description = fake.text(max_nb_chars=20)
    address = factory.SubFactory(AddressFactory)


class RegionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Region

    name = fake.name()
    prefix = fake.random_element(elements=(286, 295, 289,))
    address = factory.SubFactory(AddressFactory)


class PersonalDataFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PersonalData

    name = fake.name()
    last_name = fake.last_name()
    address = factory.SubFactory(AddressFactory)


class DepartmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Department

    name = fake.name()
    description = fake.text(max_nb_chars=20)


class EmployeeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Employee

    position = fake.text(max_nb_chars=20)
    hire_date = fake.date()
    personal_data = factory.SubFactory(PersonalDataFactory)
    department = factory.SubFactory(DepartmentFactory)


class ContractFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Contract

    number = fake.random_element(elements=(5363, 5079, 4500))
    name = fake.name()
    type = fake.text(max_nb_chars=20)
    start_date = fake.date()
    end_date = fake.date()
    description = fake.text(max_nb_chars=20)
    address = factory.SubFactory(AddressFactory)
    customer = factory.SubFactory(CustomerFactory)
    region = factory.SubFactory(RegionFactory)

    @factory.post_generation
    def employee(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for employee in extracted:
                self.employee.add(employee)


class BuildingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Building

    name = fake.name()
    description = fake.text(max_nb_chars=20)
    contract = factory.SubFactory(ContractFactory)


class DrawingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Drawing

    number = fake.random_element(elements=(1210, 1211, 1345))
    element = fake.text(max_nb_chars=20)
    revision = 'a'
    creation_date = fake.date_time(tzinfo=pytz.UTC)
    modification_date = fake.date_time(tzinfo=pytz.UTC)
    technician = factory.SubFactory(EmployeeFactory)
    building = factory.SubFactory(BuildingFactory)
    contract = factory.SubFactory(ContractFactory)
