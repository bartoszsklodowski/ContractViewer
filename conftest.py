import pytest
from django.contrib.auth.models import User
from pytest_factoryboy import register
from tests.factories import UserFactory, AddressFactory, CustomerFactory, RegionFactory, PersonalDataFactory
from tests.factories import DepartmentFactory, EmployeeFactory, ContractFactory, BuildingFactory
from tests.factories import DrawingFactory
from django_dynamic_fixture import G

register(UserFactory)
register(AddressFactory)
register(CustomerFactory)
register(RegionFactory)
register(PersonalDataFactory)
register(DepartmentFactory)
register(EmployeeFactory)
register(ContractFactory)
register(BuildingFactory)
register(DrawingFactory)


@pytest.fixture
def new_user(db, user_factory):
    user = user_factory.create()
    user.set_password("new-password")
    return user

@pytest.fixture
def authenticated_user(client):
    """Create an authenticated user for a test"""
    user = G(User, username='my_username')
    user.set_password('my_password123')
    user.save()
    client.login(username='my_username', password='my_password123')
    return user