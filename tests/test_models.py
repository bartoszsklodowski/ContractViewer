import pytest


def test_new_user(new_user):
    assert new_user.check_password("new-password") is True


def test_address(db, address_factory):
    address = address_factory.create()
    assert address


def test_customer(db, customer_factory):
    customer = customer_factory.create()
    assert customer


def test_region(db, region_factory):
    region = region_factory.create()
    assert region


def test_personal_data(db, personal_data_factory):
    personal_data = personal_data_factory.create()
    assert personal_data


def test_department(db, department_factory):
    department = department_factory.create()
    assert department


def test_employee(db, employee_factory):
    employee = employee_factory.create()
    assert employee


def test_contract(db, contract_factory, employee_factory):
    employee1 = employee_factory.create()
    employee2 = employee_factory.create()
    contract = contract_factory.create(employee=(employee1, employee2))
    assert contract


def test_building(db, building_factory):
    building = building_factory.create()
    assert building


def test_drawing(db, drawing_factory):
    drawing = drawing_factory.create()
    assert drawing
