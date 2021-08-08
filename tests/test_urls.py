import pytest
from django.urls import reverse, resolve
from .factories import AddressFactory, CustomerFactory, RegionFactory, PersonalDataFactory
from .factories import DepartmentFactory, EmployeeFactory, ContractFactory, BuildingFactory
from .factories import DrawingFactory


# accounts URLS
def test_registration_url(client):
    url = reverse('accounts:registration')
    response = client.get(url)
    assert resolve(url).view_name == 'accounts:registration'
    assert response.status_code == 200


# ContractViewer URLS
@pytest.mark.parametrize('url_name', [
    ('homepage'),
    ('password_reset'),
    ('dashboard'),
])
def test_contractviewer_urls_not_need_authenticated(url_name, client):
    url = reverse(url_name)
    response = client.get(url)
    assert resolve(url).view_name == url_name
    assert response.status_code == 200


@pytest.mark.parametrize('url_name', [
    ('search_contracts'),
    ('insert_data'),
])
def test_contractviewer_urls_need_authenticated(url_name, client):
    url = reverse(url_name)
    response = client.get(url)
    assert resolve(url).view_name == url_name
    assert response.status_code == 302


# contracts URLS
@pytest.mark.django_db
@pytest.mark.parametrize('url_name', [
    ('contracts:index'),
    ('contracts:addresses'),
    ('contracts:customers'),
    ('contracts:regions'),
    ('contracts:personal_datas'),
    ('contracts:departments'),
    ('contracts:employees'),
    ('contracts:contracts'),
    ('contracts:buildings'),
    ('contracts:drawings'),
    ('contracts:address-create-view'),
    ('contracts:customer-create-view'),
    ('contracts:region-create-view'),
    ('contracts:personal_data-create-view'),
    ('contracts:department-create-view'),
    ('contracts:employee-create-view'),
    ('contracts:contract-create-view'),
    ('contracts:building-create-view'),
    ('contracts:drawing-create-view'),
])
def test_view_url_without_pk_unauthenticated(url_name, client):
    url = reverse(url_name)
    response = client.get(url)
    assert resolve(url).view_name == url_name
    assert response.status_code == 302


@pytest.mark.django_db
@pytest.mark.parametrize('url_name', [
    ('contracts:addresses'),
    ('contracts:customers'),
    ('contracts:regions'),
    ('contracts:personal_datas'),
    ('contracts:departments'),
    ('contracts:employees'),
    ('contracts:contracts'),
    ('contracts:buildings'),
    ('contracts:drawings'),
    ('contracts:address-create-view'),
    ('contracts:customer-create-view'),
    ('contracts:region-create-view'),
    ('contracts:personal_data-create-view'),
    ('contracts:department-create-view'),
    ('contracts:employee-create-view'),
    ('contracts:contract-create-view'),
    ('contracts:building-create-view'),
    ('contracts:drawing-create-view'),
])
def test_view_url_without_pk_authenticated_without_permissions(url_name, client,
                                                               authenticated_user_without_permissions):
    url = reverse(url_name)
    response = client.get(url)
    assert resolve(url).view_name == url_name
    assert response.status_code == 403


@pytest.mark.django_db
@pytest.mark.parametrize('url_name', [
    ('contracts:index'),
    ('contracts:addresses'),
    ('contracts:customers'),
    ('contracts:regions'),
    ('contracts:personal_datas'),
    ('contracts:departments'),
    ('contracts:employees'),
    ('contracts:contracts'),
    ('contracts:buildings'),
    ('contracts:drawings'),
    ('contracts:address-create-view'),
    ('contracts:customer-create-view'),
    ('contracts:region-create-view'),
    ('contracts:personal_data-create-view'),
    ('contracts:department-create-view'),
    ('contracts:employee-create-view'),
    ('contracts:contract-create-view'),
    ('contracts:building-create-view'),
    ('contracts:drawing-create-view'),
])
def test_view_url_without_pk_authenticated_with_permissions(url_name, client, authenticated_super_user):
    url = reverse(url_name)
    response = client.get(url)
    assert resolve(url).view_name == url_name
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.parametrize('url_name', [
    ('contracts:address-detail-view'),
    ('contracts:customer-detail-view'),
    ('contracts:region-detail-view'),
    ('contracts:personal_data-detail-view'),
    ('contracts:department-detail-view'),
    ('contracts:employee-detail-view'),
    ('contracts:contract-detail-view'),
    ('contracts:building-detail-view'),
    ('contracts:drawing-detail-view'),
    ('contracts:address-update-view'),
    ('contracts:customer-update-view'),
    ('contracts:region-update-view'),
    ('contracts:personal_data-update-view'),
    ('contracts:department-update-view'),
    ('contracts:employee-update-view'),
    ('contracts:contract-update-view'),
    ('contracts:building-update-view'),
    ('contracts:drawing-update-view'),
    ('contracts:address-delete-view'),
    ('contracts:customer-delete-view'),
    ('contracts:region-delete-view'),
    ('contracts:personal_data-delete-view'),
    ('contracts:department-delete-view'),
    ('contracts:employee-delete-view'),
    ('contracts:contract-delete-view'),
    ('contracts:building-delete-view'),
    ('contracts:drawing-delete-view'),
])
def test_view_url_with_pk_unauthenticated(url_name, client):
    url = reverse(url_name, kwargs={'pk': 1})
    response = client.get(url)
    assert resolve(url).view_name == url_name
    assert response.status_code == 302


@pytest.mark.django_db
@pytest.mark.parametrize('url_name', [
    ('contracts:address-detail-view'),
    ('contracts:customer-detail-view'),
    ('contracts:region-detail-view'),
    ('contracts:personal_data-detail-view'),
    ('contracts:department-detail-view'),
    ('contracts:employee-detail-view'),
    ('contracts:contract-detail-view'),
    ('contracts:building-detail-view'),
    ('contracts:drawing-detail-view'),
    ('contracts:address-update-view'),
    ('contracts:customer-update-view'),
    ('contracts:region-update-view'),
    ('contracts:personal_data-update-view'),
    ('contracts:department-update-view'),
    ('contracts:employee-update-view'),
    ('contracts:contract-update-view'),
    ('contracts:building-update-view'),
    ('contracts:drawing-update-view'),
    ('contracts:address-delete-view'),
    ('contracts:customer-delete-view'),
    ('contracts:region-delete-view'),
    ('contracts:personal_data-delete-view'),
    ('contracts:department-delete-view'),
    ('contracts:employee-delete-view'),
    ('contracts:contract-delete-view'),
    ('contracts:building-delete-view'),
    ('contracts:drawing-delete-view'),
])
def test_view_url_with_pk_authenticated_without_permissions(url_name, client, authenticated_user_without_permissions):
    url = reverse(url_name, kwargs={'pk': 1})
    response = client.get(url)
    assert resolve(url).view_name == url_name
    assert response.status_code == 403


@pytest.mark.django_db
def test_view_url_with_pk_authenticated_with_permissions_address(client, authenticated_super_user, address_factory):
    address_factory.create()
    url = reverse('contracts:address-detail-view', kwargs={'pk': 1})
    response = client.get(url)
    assert resolve(url).view_name == 'contracts:address-detail-view'
    assert response.status_code == 200

    url = reverse('contracts:address-update-view', kwargs={'pk': 1})
    response = client.get(url)
    assert resolve(url).view_name == 'contracts:address-update-view'
    assert response.status_code == 200

    url = reverse('contracts:address-delete-view', kwargs={'pk': 1})
    response = client.get(url)
    assert resolve(url).view_name == 'contracts:address-delete-view'
    assert response.status_code == 200


@pytest.mark.django_db
def test_view_url_with_pk_authenticated_with_permissions_region(client, authenticated_super_user, region_factory):
    region_factory.create()
    url = reverse('contracts:region-detail-view', kwargs={'pk': 1})
    response = client.get(url)
    assert resolve(url).view_name == 'contracts:region-detail-view'
    assert response.status_code == 200

    url = reverse('contracts:region-update-view', kwargs={'pk': 1})
    response = client.get(url)
    assert resolve(url).view_name == 'contracts:region-update-view'
    assert response.status_code == 200

    url = reverse('contracts:region-delete-view', kwargs={'pk': 1})
    response = client.get(url)
    assert resolve(url).view_name == 'contracts:region-delete-view'
    assert response.status_code == 200


@pytest.mark.django_db
def test_view_url_with_pk_authenticated_with_permissions_customer(client, authenticated_super_user, customer_factory):
    customer_factory.create()
    url = reverse('contracts:customer-detail-view', kwargs={'pk': 1})
    response = client.get(url)
    assert resolve(url).view_name == 'contracts:customer-detail-view'
    assert response.status_code == 200

    url = reverse('contracts:customer-update-view', kwargs={'pk': 1})
    response = client.get(url)
    assert resolve(url).view_name == 'contracts:customer-update-view'
    assert response.status_code == 200

    url = reverse('contracts:customer-delete-view', kwargs={'pk': 1})
    response = client.get(url)
    assert resolve(url).view_name == 'contracts:customer-delete-view'
    assert response.status_code == 200


@pytest.mark.django_db
def test_view_url_with_pk_authenticated_with_permissions_personal_data(client, authenticated_super_user,
                                                                       personal_data_factory):
    personal_data_factory.create()
    url = reverse('contracts:personal_data-detail-view', kwargs={'pk': 1})
    response = client.get(url)
    assert resolve(url).view_name == 'contracts:personal_data-detail-view'
    assert response.status_code == 200

    url = reverse('contracts:personal_data-update-view', kwargs={'pk': 1})
    response = client.get(url)
    assert resolve(url).view_name == 'contracts:personal_data-update-view'
    assert response.status_code == 200

    url = reverse('contracts:personal_data-delete-view', kwargs={'pk': 1})
    response = client.get(url)
    assert resolve(url).view_name == 'contracts:personal_data-delete-view'
    assert response.status_code == 200


@pytest.mark.django_db
def test_view_url_with_pk_authenticated_with_permissions_department(client, authenticated_super_user,
                                                                    department_factory):
    department_factory.create()
    url = reverse('contracts:department-detail-view', kwargs={'pk': 1})
    response = client.get(url)
    assert resolve(url).view_name == 'contracts:department-detail-view'
    assert response.status_code == 200

    url = reverse('contracts:department-update-view', kwargs={'pk': 1})
    response = client.get(url)
    assert resolve(url).view_name == 'contracts:department-update-view'
    assert response.status_code == 200

    url = reverse('contracts:department-delete-view', kwargs={'pk': 1})
    response = client.get(url)
    assert resolve(url).view_name == 'contracts:department-delete-view'
    assert response.status_code == 200


@pytest.mark.django_db
def test_view_url_with_pk_authenticated_with_permissions_employee(client, authenticated_super_user, employee_factory):
    employee_factory.create()
    url = reverse('contracts:employee-detail-view', kwargs={'pk': 1})
    response = client.get(url)
    assert resolve(url).view_name == 'contracts:employee-detail-view'
    assert response.status_code == 200

    url = reverse('contracts:employee-update-view', kwargs={'pk': 1})
    response = client.get(url)
    assert resolve(url).view_name == 'contracts:employee-update-view'
    assert response.status_code == 200

    url = reverse('contracts:employee-delete-view', kwargs={'pk': 1})
    response = client.get(url)
    assert resolve(url).view_name == 'contracts:employee-delete-view'
    assert response.status_code == 200


@pytest.mark.django_db
def test_view_url_with_pk_authenticated_with_permissions_contract(client, authenticated_super_user, contract_factory):
    contract_factory.create()
    url = reverse('contracts:contract-detail-view', kwargs={'pk': 1})
    response = client.get(url)
    assert resolve(url).view_name == 'contracts:contract-detail-view'
    assert response.status_code == 200

    url = reverse('contracts:contract-update-view', kwargs={'pk': 1})
    response = client.get(url)
    assert resolve(url).view_name == 'contracts:contract-update-view'
    assert response.status_code == 200

    url = reverse('contracts:contract-delete-view', kwargs={'pk': 1})
    response = client.get(url)
    assert resolve(url).view_name == 'contracts:contract-delete-view'
    assert response.status_code == 200


@pytest.mark.django_db
def test_view_url_with_pk_authenticated_with_permissions_building(client, authenticated_super_user, building_factory):
    building_factory.create()
    url = reverse('contracts:building-detail-view', kwargs={'pk': 1})
    response = client.get(url)
    assert resolve(url).view_name == 'contracts:building-detail-view'
    assert response.status_code == 200

    url = reverse('contracts:building-update-view', kwargs={'pk': 1})
    response = client.get(url)
    assert resolve(url).view_name == 'contracts:building-update-view'
    assert response.status_code == 200

    url = reverse('contracts:building-delete-view', kwargs={'pk': 1})
    response = client.get(url)
    assert resolve(url).view_name == 'contracts:building-delete-view'
    assert response.status_code == 200


@pytest.mark.django_db
def test_view_url_with_pk_authenticated_with_permissions_drawing(client, authenticated_super_user, drawing_factory):
    drawing_factory.create()
    url = reverse('contracts:drawing-detail-view', kwargs={'pk': 1})
    response = client.get(url)
    assert resolve(url).view_name == 'contracts:drawing-detail-view'
    assert response.status_code == 200

    url = reverse('contracts:drawing-update-view', kwargs={'pk': 1})
    response = client.get(url)
    assert resolve(url).view_name == 'contracts:drawing-update-view'
    assert response.status_code == 200

    url = reverse('contracts:drawing-delete-view', kwargs={'pk': 1})
    response = client.get(url)
    assert resolve(url).view_name == 'contracts:drawing-delete-view'
    assert response.status_code == 200
