from django.forms import CharField, Form, DateTimeField, ModelChoiceField, TextInput, ModelForm, IntegerField
from django.forms import ModelMultipleChoiceField, CheckboxSelectMultiple, SelectDateWidget
from contracts.models import Address, Customer, Region, PersonalData, Department, Employee, Contract, Building, Drawing
from django.core.exceptions import ValidationError


class AddressModelForm(ModelForm):
    class Meta:
        model = Address
        fields = "__all__"


class CustomerModelForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class RegionModelForm(ModelForm):
    class Meta:
        model = Region
        fields = "__all__"


class PersonalDataModelForm(ModelForm):
    class Meta:
        model = PersonalData
        fields = "__all__"


class DepartmentModelForm(ModelForm):
    class Meta:
        model = Department
        fields = "__all__"


class EmployeeModelForm(ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {"hire_date": SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),
                                                 years=range(1990, 2030))}


class ContractModelForm(ModelForm):
    class Meta:
        model = Contract
        fields = "__all__"
        widgets = {"employee": CheckboxSelectMultiple,
                   "start_date": SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),
                                                  years=range(1990, 2030)),
                   "end_date": SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),
                                                years=range(1990, 2030))}


class BuildingModelForm(ModelForm):
    class Meta:
        model = Building
        fields = "__all__"


class DrawingModelForm(ModelForm):
    class Meta:
        model = Drawing
        fields = "__all__"
        widgets = {"modification_date": SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),
                                                         years=range(1990, 2030))}
