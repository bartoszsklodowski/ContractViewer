import django_filters
from contracts.models import Address, Customer, Region, PersonalData, Department, Employee, Contract, Building, Drawing
from django.forms import CheckboxSelectMultiple, SelectDateWidget

CHOICES = (
    ('ascending', 'Ascending'),
    ('descending', 'Descending')
)


class AddressFilter(django_filters.FilterSet):
    street = django_filters.CharFilter(field_name='street', label="Street", lookup_expr='icontains')
    zip_code = django_filters.CharFilter(field_name='zip_code', label="Zipcode", lookup_expr='icontains')
    town = django_filters.CharFilter(field_name='town', label="Town", lookup_expr='icontains')
    ordering = django_filters.ChoiceFilter(label="Ordering", choices=CHOICES, method='filter_by_order')

    class Meta:
        model = Address
        fields = {}

    def filter_by_order(self, queryset, name, value):
        expression = 'town' if value == 'ascending' else '-town'
        return queryset.order_by(expression)


class CustomerFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', label="Name", lookup_expr='icontains')
    ordering = django_filters.ChoiceFilter(label="Ordering", choices=CHOICES, method='filter_by_order')

    class Meta:
        model = Customer
        fields = {}

    def filter_by_order(self, queryset, name, value):
        expression = 'name' if value == 'ascending' else '-name'
        return queryset.order_by(expression)


class RegionFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', label="Name", lookup_expr='icontains')
    prefix = django_filters.CharFilter(field_name='prefix', label="Prefix", lookup_expr='icontains')
    address = django_filters.CharFilter(field_name='address__town', label="Address Town", lookup_expr='icontains')
    ordering = django_filters.ChoiceFilter(label="Ordering", choices=CHOICES, method='filter_by_order')

    class Meta:
        model = Region
        fields = {}

    def filter_by_order(self, queryset, name, value):
        expression = 'prefix' if value == 'ascending' else '-prefix'
        return queryset.order_by(expression)


class PersonalDataFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', label="Name", lookup_expr='icontains')
    last_name = django_filters.CharFilter(field_name='last_name', label="Last_name", lookup_expr='icontains')
    address = django_filters.CharFilter(field_name='address__town', label="Address Town", lookup_expr='icontains')
    ordering = django_filters.ChoiceFilter(label="Ordering", choices=CHOICES, method='filter_by_order')

    class Meta:
        model = PersonalData
        fields = {}

    def filter_by_order(self, queryset, name, value):
        expression = 'last_name' if value == 'ascending' else '-last_name'
        return queryset.order_by(expression)


class DepartmentFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', label="Name", lookup_expr='icontains')
    ordering = django_filters.ChoiceFilter(label="Ordering", choices=CHOICES, method='filter_by_order')

    class Meta:
        model = Department
        fields = {}

    def filter_by_order(self, queryset, name, value):
        expression = 'name' if value == 'ascending' else '-name'
        return queryset.order_by(expression)


class EmployeeFilter(django_filters.FilterSet):
    position = django_filters.CharFilter(field_name='position', label="Position", lookup_expr='icontains')
    hire_date = django_filters.DateFilter(field_name='hire_date', label="Hire Date", lookup_expr='icontains',
                                          widget=SelectDateWidget(
                                              empty_label=("Choose Year", "Choose Month", "Choose Day"),
                                              years=range(1990, 2030)))
    personal_data = django_filters.CharFilter(field_name='personal_data__name', label="Personal Data Name",
                                              lookup_expr='icontains')
    department = django_filters.CharFilter(field_name='department__name', label="Department Name",
                                           lookup_expr='icontains')
    ordering = django_filters.ChoiceFilter(label="Ordering", choices=CHOICES, method='filter_by_order')

    class Meta:
        model = Employee
        fields = {}

    def filter_by_order(self, queryset, name, value):
        expression = 'personal_data__last_name' if value == 'ascending' else '-personal_data__last_name'
        return queryset.order_by(expression)


class ContractFilter(django_filters.FilterSet):
    number = django_filters.CharFilter(field_name='number', label="Number", lookup_expr='icontains')
    name = django_filters.CharFilter(field_name='name', label="Name", lookup_expr='icontains')
    type = django_filters.CharFilter(field_name='type', label="Type", lookup_expr='icontains')
    start_date = django_filters.DateFilter(field_name='start_date', label="Start Date", lookup_expr='icontains',
                                           widget=SelectDateWidget(
                                               empty_label=("Choose Year", "Choose Month", "Choose Day"),
                                               years=range(1990, 2030)))
    end_date = django_filters.DateFilter(field_name='end_date', label="End Date", lookup_expr='icontains',
                                         widget=SelectDateWidget(
                                             empty_label=("Choose Year", "Choose Month", "Choose Day"),
                                             years=range(1990, 2030)))
    address = django_filters.CharFilter(field_name='address__town')
    customer = django_filters.CharFilter(field_name='customer__name')
    region = django_filters.CharFilter(field_name='region__name')
    employee = django_filters.ModelMultipleChoiceFilter(queryset=Employee.objects.all(), field_name='address',
                                                        widget=CheckboxSelectMultiple(),
                                                        label="Employees",
                                                        label_suffix="", )
    ordering = django_filters.ChoiceFilter(label="Ordering", choices=CHOICES, method='filter_by_order')

    class Meta:
        model = Contract
        fields = {}

    def filter_by_order(self, queryset, name, value):
        expression = 'number' if value == 'ascending' else '-number'
        return queryset.order_by(expression)


class BuildingFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', label="Name", lookup_expr='icontains')
    contract = django_filters.CharFilter(field_name='contract__number', label="Contract Number",
                                         lookup_expr='icontains')
    ordering = django_filters.ChoiceFilter(label="Ordering", choices=CHOICES, method='filter_by_order')

    class Meta:
        model = Building
        fields = {}

    def filter_by_order(self, queryset, name, value):
        expression = 'name' if value == 'ascending' else '-name'
        return queryset.order_by(expression)


class DrawingFilter(django_filters.FilterSet):
    number = django_filters.CharFilter(field_name='number', label="Number", lookup_expr='icontains')
    element = django_filters.CharFilter(field_name='element', label="Element", lookup_expr='icontains')
    revision = django_filters.CharFilter(field_name='revision', label="Revision", lookup_expr='icontains')
    creation_date = django_filters.DateFilter(field_name='creation_date', label="Creation Date",
                                              lookup_expr='icontains',
                                              widget=SelectDateWidget(
                                                  empty_label=("Choose Year", "Choose Month", "Choose Day"),
                                                  years=range(1990, 2030)))
    modification_date = django_filters.DateFilter(field_name='modification_date', label="Modification Date",
                                                  lookup_expr='icontains',
                                                  widget=SelectDateWidget(
                                                      empty_label=("Choose Year", "Choose Month", "Choose Day"),
                                                      years=range(1990, 2030)))
    technician = django_filters.CharFilter(field_name='technician__personal_data__last_name',
                                           label="Technician Last Name", lookup_expr='icontains')
    building = django_filters.CharFilter(field_name='building__name', label="Building Name", lookup_expr='icontains')
    contract = django_filters.CharFilter(field_name='contract__number', label="Contract Number",
                                         lookup_expr='icontains')
    ordering = django_filters.ChoiceFilter(label="Ordering", choices=CHOICES, method='filter_by_order')

    class Meta:
        model = Drawing
        fields = {}

    def filter_by_order(self, queryset, name, value):
        expression = 'number' if value == 'ascending' else '-number'
        return queryset.order_by(expression)
