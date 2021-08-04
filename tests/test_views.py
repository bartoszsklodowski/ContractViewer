from urllib import request

from django.contrib.auth.models import User, AnonymousUser
from mixer.backend.django import mixer
import pytest
from django import urls
from django.contrib.auth import get_user_model
from django.core import mail
from django.urls import reverse
from contracts.views import insert_data, index_contracts, contract_multiple_view, homepage

# ACCOUNTS

@pytest.mark.django_db
def test_user_signup(client, user_factory, staff_group_factory):
    user_model = get_user_model()
    group = staff_group_factory.create()
    assert user_model.objects.count() == 0
    signup_url = urls.reverse('accounts:registration')
    resp = client.post(signup_url,
                       {'username': user_factory.username, 'password1': user_factory.password,
                        'password2': user_factory.password, 'email': user_factory.email})
    assert user_model.objects.count() == 1
    for user in user_model.objects.filter(pk=1):
        assert user.groups.filter(name="Staff").exists()
    assert resp.status_code == 302


@pytest.mark.django_db
def test_user_login(client, new_user):
    user_model = get_user_model()
    assert user_model.objects.count() == 1
    resp = client.post('/accounts/login/',
                       data={'username': new_user.username, 'password': 'new-password'})
    assert resp.status_code == 302
    assert resp.url == 'dashboard/'


@pytest.mark.django_db
def test_user_logout(client, authenticated_user):
    resp = client.get('/accounts/logout/')
    assert resp.status_code == 302
    assert resp.url == 'dashboard/'


@pytest.mark.django_db
def test_user_reset_password(client, new_user):
    user_model = get_user_model()
    assert user_model.objects.count() == 1
    resp = client.post('/accounts/password_reset/', data={'email': new_user.email})
    assert len(mail.outbox) == 1
    assert mail.outbox[0].subject == 'ContractViewer password confirmation link'
    assert mail.outbox[0].to[0] == new_user.email
    assert resp.status_code == 302
    assert resp.url == '/accounts/password_reset/done/'


@pytest.mark.django_db
def test_user_reset_password_wrong_email(client, new_user):
    user_model = get_user_model()
    assert user_model.objects.count() == 1
    resp = client.post('/accounts/password_reset/', data={'email': 'example@gmail.com'})
    assert len(mail.outbox) == 0
    assert resp.status_code == 200


#CONTRACTS

def test_insert_data_authenticated(db, factory):
    path = reverse('insert_data')
    request = factory.get(path)
    request.user = mixer.blend(User)

    response = insert_data(request)
    assert response.status_code == 200


def test_insert_data_unauthenticated(factory):
    path = reverse('insert_data')
    request = factory.get(path)
    request.user = AnonymousUser()

    response = insert_data(request)
    assert 'accounts/login' in response.url


def test_index_contracts_authenticated(db, factory):
    path = reverse('contracts:index')
    request = factory.get(path)
    request.user = mixer.blend(User)

    response = index_contracts(request)
    assert response.status_code == 200


def test_index_contracts_unauthenticated(factory):
    path = reverse('contracts:index')
    request = factory.get(path)
    request.user = AnonymousUser()

    response = index_contracts(request)
    assert 'accounts/login' in response.url


def test_contract_multiple_view_authenticated(db, factory):
    path = reverse('contracts:contract-multiple-view')
    request = factory.get(path)
    request.user = mixer.blend(User)

    response = contract_multiple_view(request)
    assert response.status_code == 200


def test_contract_multiple_view_unauthenticated(factory):
    path = reverse('contracts:contract-multiple-view')
    request = factory.get(path)
    request.user = AnonymousUser()

    response = contract_multiple_view(request)
    assert 'accounts/login' in response.url


def test_homepage_view(db, factory):
    path = reverse('homepage')
    request = factory.get(path)

    response = homepage(request)
    assert response.status_code == 200