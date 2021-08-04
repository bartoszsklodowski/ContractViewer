import pytest
from django.urls import reverse, resolve


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
def test_view_url_without_pk_authenticated_with_permissions(url_name, client, authenticated_super_user, address_factory,
                                                            customer_factory, region_factory, personal_data_factory,
                                                            department_factory, employee_factory, contract_factory,
                                                            building_factory, drawing_factory):
    address_factory.create()
    customer_factory.create()
    region_factory.create()
    personal_data_factory.create()
    department_factory.create()
    employee_factory.create()
    contract_factory.create()
    building_factory.create()
    drawing_factory.create()
    url = reverse(url_name)
    response = client.get(url)
    assert resolve(url).view_name == url_name
    assert response.status_code == 200


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
def test_view_url_with_pk_authenticated_with_permissions(url_name, client, authenticated_super_user, address_factory,
                                                         customer_factory, region_factory, personal_data_factory,
                                                         department_factory, employee_factory, contract_factory,
                                                         building_factory, drawing_factory):
    address_factory.create()
    customer_factory.create()
    region_factory.create()
    personal_data_factory.create()
    department_factory.create()
    employee_factory.create()
    contract_factory.create()
    building_factory.create()
    drawing_factory.create()
    url = reverse(url_name, kwargs={'pk': 1})
    response = client.get(url)
    assert resolve(url).view_name == url_name
    assert response.status_code == 200
