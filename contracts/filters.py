import django_filters
from contracts.models import Address, Customer, Region, PersonalData, Department, Employee, Contract, Building, Drawing
from django.forms import CheckboxSelectMultiple
from django.forms.widgets import TextInput, DateInput

CHOICES = (
    ('ascending', 'Ascending'),
    ('descending', 'Descending')
)


class AddressFilter(django_filters.FilterSet):
    street = django_filters.CharFilter(field_name='street', label="", lookup_expr='icontains',
                                       widget=TextInput(attrs={'placeholder': 'Street'}))
    zip_code = django_filters.CharFilter(field_name='zip_code', label="", lookup_expr='icontains',
                                         widget=TextInput(attrs={'placeholder': 'Zip code'}))
    town = django_filters.CharFilter(field_name='town', label="", lookup_expr='icontains',
                                     widget=TextInput(attrs={'placeholder': 'Town'}))
    ordering = django_filters.ChoiceFilter(label="Ordering", choices=CHOICES, method='filter_by_order')

    class Meta:
        model = Address
        fields = {}

    def filter_by_order(self, queryset, name, value):
        expression = 'town' if value == 'ascending' else '-town'
        return queryset.order_by(expression)


class CustomerFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', label="", lookup_expr='icontains',
                                     widget=TextInput(attrs={'placeholder': 'Name'}))
    ordering = django_filters.ChoiceFilter(label="Ordering", choices=CHOICES, method='filter_by_order')

    class Meta:
        model = Customer
        fields = {}

    def filter_by_order(self, queryset, name, value):
        expression = 'name' if value == 'ascending' else '-name'
        return queryset.order_by(expression)


class RegionFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', label="", lookup_expr='icontains',
                                     widget=TextInput(attrs={'placeholder': 'Name'}))
    prefix = django_filters.CharFilter(field_name='prefix', label="", lookup_expr='icontains',
                                       widget=TextInput(attrs={'placeholder': 'Prefix'}))
    address = django_filters.CharFilter(field_name='address__town', label="", lookup_expr='icontains',
                                        widget=TextInput(attrs={'placeholder': 'Address Town'}))
    ordering = django_filters.ChoiceFilter(label="Ordering", choices=CHOICES, method='filter_by_order')

    class Meta:
        model = Region
        fields = {}

    def filter_by_order(self, queryset, name, value):
        expression = 'prefix' if value == 'ascending' else '-prefix'
        return queryset.order_by(expression)


class PersonalDataFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', label="", lookup_expr='icontains',
                                     widget=TextInput(attrs={'placeholder': 'Name'}))
    last_name = django_filters.CharFilter(field_name='last_name', label="", lookup_expr='icontains',
                                          widget=TextInput(attrs={'placeholder': 'Last_name'}))
    address = django_filters.CharFilter(field_name='address__town', label="", lookup_expr='icontains',
                                        widget=TextInput(attrs={'placeholder': 'Address Town'}))
    ordering = django_filters.ChoiceFilter(label="Ordering", choices=CHOICES, method='filter_by_order')

    class Meta:
        model = PersonalData
        fields = {}

    def filter_by_order(self, queryset, name, value):
        expression = 'last_name' if value == 'ascending' else '-last_name'
        return queryset.order_by(expression)


class DepartmentFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', label="", lookup_expr='icontains',
                                     widget=TextInput(attrs={'placeholder': 'Name'}))
    ordering = django_filters.ChoiceFilter(label="Ordering", choices=CHOICES, method='filter_by_order')

    class Meta:
        model = Department
        fields = {}

    def filter_by_order(self, queryset, name, value):
        expression = 'name' if value == 'ascending' else '-name'
        return queryset.order_by(expression)


class EmployeeFilter(django_filters.FilterSet):
    position = django_filters.CharFilter(field_name='position', label="", lookup_expr='icontains',
                                         widget=TextInput(attrs={'placeholder': 'Position'}))
    hire_date = django_filters.DateFilter(field_name='hire_date', label="Hire Date", lookup_expr='icontains',
                                          widget=DateInput(attrs={'type': 'date'}))
    personal_data = django_filters.CharFilter(field_name='personal_data__name', label="",
                                              lookup_expr='icontains',
                                              widget=TextInput(attrs={'placeholder': 'Personal Data Name'}))
    department = django_filters.CharFilter(field_name='department__name', label="",
                                           lookup_expr='icontains',
                                           widget=TextInput(attrs={'placeholder': 'Department Name'}))
    ordering = django_filters.ChoiceFilter(label="Ordering", choices=CHOICES, method='filter_by_order')

    class Meta:
        model = Employee
        fields = {}

    def filter_by_order(self, queryset, name, value):
        expression = 'personal_data__last_name' if value == 'ascending' else '-personal_data__last_name'
        return queryset.order_by(expression)


class ContractFilter(django_filters.FilterSet):
    number = django_filters.CharFilter(field_name='number', label="", lookup_expr='icontains',
                                       widget=TextInput(attrs={'placeholder': 'Number'}))
    name = django_filters.CharFilter(field_name='name', label="", lookup_expr='icontains',
                                     widget=TextInput(attrs={'placeholder': 'Name'}))
    type = django_filters.CharFilter(field_name='type', label="", lookup_expr='icontains',
                                     widget=TextInput(attrs={'placeholder': 'Type'}))
    start_date = django_filters.DateFilter(field_name='start_date', label="Start Date", lookup_expr='icontains',
                                           widget=DateInput(attrs={'type': 'date'}))
    end_date = django_filters.DateFilter(field_name='end_date', label="End Date", lookup_expr='icontains',
                                         widget=DateInput(attrs={'type': 'date'}))
    address = django_filters.CharFilter(field_name='address__town', label="",
                                        widget=TextInput(attrs={'placeholder': 'Address town'}))
    customer = django_filters.CharFilter(field_name='customer__name', label="",
                                         widget=TextInput(attrs={'placeholder': 'Customer name'}))
    region = django_filters.CharFilter(field_name='region__name', label="",
                                       widget=TextInput(attrs={'placeholder': 'Region name'}))
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
    name = django_filters.CharFilter(field_name='name', label="", lookup_expr='icontains',
                                     widget=TextInput(attrs={'placeholder': 'Name'}))
    contract = django_filters.CharFilter(field_name='contract__number', label="",
                                         lookup_expr='icontains',
                                         widget=TextInput(attrs={'placeholder': 'Contract number'}))
    ordering = django_filters.ChoiceFilter(label="Ordering", choices=CHOICES, method='filter_by_order')

    class Meta:
        model = Building
        fields = {}

    def filter_by_order(self, queryset, name, value):
        expression = 'name' if value == 'ascending' else '-name'
        return queryset.order_by(expression)


class DrawingFilter(django_filters.FilterSet):
    number = django_filters.CharFilter(field_name='number', label="", lookup_expr='icontains',
                                       widget=TextInput(attrs={'placeholder': 'Number'}))
    element = django_filters.CharFilter(field_name='element', label="", lookup_expr='icontains',
                                        widget=TextInput(attrs={'placeholder': 'Element'}))
    revision = django_filters.CharFilter(field_name='revision', label="", lookup_expr='icontains',
                                         widget=TextInput(attrs={'placeholder': 'Revision'}))
    creation_date = django_filters.DateFilter(field_name='creation_date', label="Creation Date",
                                              lookup_expr='icontains',
                                              widget=DateInput(attrs={'type': 'date'}))
    modification_date = django_filters.DateFilter(field_name='modification_date', label="Modification Date",
                                                  lookup_expr='icontains',
                                                  widget=DateInput(attrs={'type': 'date'}))
    technician = django_filters.CharFilter(field_name='technician__personal_data__last_name',
                                           label="", lookup_expr='icontains',
                                           widget=TextInput(attrs={'placeholder': 'Technician Last Name'}))
    building = django_filters.CharFilter(field_name='building__name', label="", lookup_expr='icontains',
                                         widget=TextInput(attrs={'placeholder': 'Building Name'}))
    contract = django_filters.CharFilter(field_name='contract__number', label="",
                                         lookup_expr='icontains',
                                         widget=TextInput(attrs={'placeholder': 'Contract Number'}))
    ordering = django_filters.ChoiceFilter(label="Ordering", choices=CHOICES, method='filter_by_order')

    class Meta:
        model = Drawing
        fields = {}

    def filter_by_order(self, queryset, name, value):
        expression = 'number' if value == 'ascending' else '-number'
        return queryset.order_by(expression)
