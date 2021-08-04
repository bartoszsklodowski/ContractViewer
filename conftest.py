import pytest
from django.test import RequestFactory
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from pytest_factoryboy import register
from tests.factories import UserFactory, AddressFactory, CustomerFactory, RegionFactory, PersonalDataFactory
from tests.factories import DepartmentFactory, EmployeeFactory, ContractFactory, BuildingFactory, StaffGroupFactory
from tests.factories import DrawingFactory, SuperUserFactory

register(UserFactory)
register(SuperUserFactory)
register(StaffGroupFactory)
register(AddressFactory)
register(CustomerFactory)
register(RegionFactory)
register(PersonalDataFactory)
register(DepartmentFactory)
register(EmployeeFactory)
register(ContractFactory)
register(BuildingFactory)
register(DrawingFactory)

permissions_list = [
    ('can_view_user', 'Can view user'),
    ('can_view_address', 'Can view address'),
    ('can_add_building', 'Can add building'),
    ('can_view_building', 'Can view building'),
    ('can_add_contract', 'Can add contract'),
    ('can_view_contract', 'Can view contract'),
    ('can_view_customer', 'Can view customer'),
    ('can_view_department', 'Can view department'),
    ('can_add_drawing', 'Can add drawing'),
    ('can_delete_drawing', 'Can delete drawing'),
    ('can_view_drawing', 'Can view drawing'),
    ('can_view_employee', 'Can view employee'),
    ('can_view_region', 'Can view region')
]


@pytest.mark.django_db
def create_staff_permissions():
    return [Permission.objects.create(name=name[1], codename=name[0],
            content_type=ContentType.objects.get(model=name[1].split()[2])) for name in permissions_list]


@pytest.mark.django_db
@pytest.fixture
def new_user(db, user_factory, staff_group_factory):
    user = user_factory()
    group = staff_group_factory()
    permissions_list_created = create_staff_permissions()
    group.permissions.add(*permissions_list_created)
    user.groups.add(group)
    user.set_password("new-password")
    user.save()
    return user


@pytest.mark.django_db
@pytest.fixture
def authenticated_user(db, client, user_factory, staff_group_factory):
    user = user_factory()
    group = staff_group_factory()
    permissions_list_created = create_staff_permissions()
    group.permissions.add(*permissions_list_created)
    user.groups.add(group)
    user.set_password('my_password123')
    user.save()
    client.login(username=user.username, password='my_password123')
    return user


@pytest.mark.django_db
@pytest.fixture
def authenticated_user_without_permissions(db, client, user_factory, staff_group_factory):
    user = user_factory()
    group = staff_group_factory()
    user.groups.add(group)
    user.set_password('my_password123')
    user.save()
    client.login(username=user.username, password='my_password123')
    return user


@pytest.mark.django_db
@pytest.fixture
def authenticated_super_user(db, client, super_user_factory):
    user = super_user_factory()
    user.set_password('my_password123')
    user.save()
    client.login(username=user.username, password='my_password123')
    return user


@pytest.fixture(scope='module')
def factory():
    return RequestFactory()
