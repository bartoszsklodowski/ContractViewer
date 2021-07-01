from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, ListView, FormView, CreateView, DetailView, UpdateView, DeleteView

from contracts.models import Address, Customer, Region, PersonalData, Department, Employee, Contract, Building, Drawing
from contracts.forms import AddressModelForm, CustomerModelForm, RegionModelForm, PersonalDataModelForm, DepartmentModelForm
from contracts.forms import EmployeeModelForm, ContractModelForm, BuildingModelForm, DrawingModelForm


def homepage(request):
    return render(request, template_name="homepage.html")

# @login_required(login_url="/accounts/login/")
def index_contracts(request):
    return render(request, template_name="index_contracts.html")


# LISTVIEW
class AddressListView(ListView):
    # permission_required = ['movies.view_actor', ]
    template_name = "addresses.html"
    model = Address


class CustomerListView(ListView):
    # permission_required = ['movies.view_actor', ]
    template_name = "customers.html"
    model = Customer


class RegionListView(ListView):
    # permission_required = ['movies.view_actor', ]
    template_name = "regions.html"
    model = Region


class PersonalDataListView(ListView):
    # permission_required = ['movies.view_actor', ]
    template_name = "personal_datas.html"
    model = PersonalData


class DepartmentListView(ListView):
    # permission_required = ['movies.view_actor', ]
    template_name = "departments.html"
    model = Department


class EmployeeListView(ListView):
    # permission_required = ['movies.view_actor', ]
    template_name = "employees.html"
    model = Employee


class ContractListView(ListView):
    # permission_required = ['movies.view_actor', ]
    template_name = "contracts.html"
    model = Contract


class BuildingListView(ListView):
    # permission_required = ['movies.view_actor', ]
    template_name = "buildings.html"
    model = Building


class DrawingListView(ListView):
    # permission_required = ['movies.view_actor', ]
    template_name = "drawings.html"
    model = Drawing


# DETAILVIEW
class AddressDetailView(DetailView):
    # permission_required = ['movies.view_actor', ]
    model = Address
    template_name = "address.html"


class CustomerDetailView(DetailView):
    # permission_required = ['movies.view_actor', ]
    model = Customer
    template_name = "customer.html"


class RegionDetailView(DetailView):
    # permission_required = ['movies.view_actor', ]
    model = Region
    template_name = "region.html"


class PersonalDataDetailView(DetailView):
    # permission_required = ['movies.view_actor', ]
    model = PersonalData
    template_name = "personal_data.html"


class DepartmentDetailView(DetailView):
    # permission_required = ['movies.view_actor', ]
    model = Department
    template_name = "department.html"


class EmployeeDetailView(DetailView):
    # permission_required = ['movies.view_actor', ]
    model = Employee
    template_name = "employee.html"


class ContractDetailView(DetailView):
    # permission_required = ['movies.view_actor', ]
    model = Contract
    template_name = "contract.html"


class BuildingDetailView(DetailView):
    # permission_required = ['movies.view_actor', ]
    model = Building
    template_name = "building.html"


class DrawingDetailView(DetailView):
    # permission_required = ['movies.view_actor', ]
    model = Drawing
    template_name = "drawing.html"


# CREATEVIEW
class AddressCreateView(CreateView):
    # permission_required = ['movies.add_actor', ]
    model = Address
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index")


class CustomerCreateView(CreateView):
    # permission_required = ['movies.add_actor', ]
    model = Customer
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index")


class RegionCreateView(CreateView):
    # permission_required = ['movies.add_actor', ]
    model = Region
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index")


class PersonalDataCreateView(CreateView):
    # permission_required = ['movies.add_actor', ]
    model = PersonalData
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index")


class DepartmentCreateView(CreateView):
    # permission_required = ['movies.add_actor', ]
    model = Department
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index")


class EmployeeCreateView(CreateView):
    # permission_required = ['movies.add_actor', ]
    model = Employee
    form_class = EmployeeModelForm
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index")


class ContractCreateView(CreateView):
    # permission_required = ['movies.add_actor', ]
    model = Contract
    form_class = ContractModelForm
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index")


class BuildingCreateView(CreateView):
    # permission_required = ['movies.add_actor', ]
    model = Building
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index")


class DrawingCreateView(CreateView):
    # permission_required = ['movies.add_actor', ]
    model = Drawing
    form_class = DrawingModelForm
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index")


# UPDATEVIEW
class AddressUpdateView(UpdateView):
    # permission_required = ['movies.view_actor', 'movies.change_actor', ]
    model = Address
    fields = ("street", "zip_code", "town",)
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index_contracts")


class CustomerUpdateView(UpdateView):
    # permission_required = ['movies.view_actor', 'movies.change_actor', ]
    model = Customer
    fields = ("name", "description", "address",)
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index_contracts")


class RegionUpdateView(UpdateView):
    # permission_required = ['movies.view_actor', 'movies.change_actor', ]
    model = Region
    fields = ("name", "prefix", "address",)
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index_contracts")


class PersonalDataUpdateView(UpdateView):
    # permission_required = ['movies.view_actor', 'movies.change_actor', ]
    model = PersonalData
    fields = ("name", "last_name", "address",)
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index_contracts")


class DepartmentUpdateView(UpdateView):
    # permission_required = ['movies.view_actor', 'movies.change_actor', ]
    model = Department
    fields = ("name", "description",)
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index_contracts")


class EmployeeUpdateView(UpdateView):
    # permission_required = ['movies.view_actor', 'movies.change_actor', ]
    model = Employee
    form_class = EmployeeModelForm
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index_contracts")


class ContractUpdateView(UpdateView):
    # permission_required = ['movies.view_actor', 'movies.change_actor', ]
    model = Contract
    form_class = ContractModelForm
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index_contracts")


class BuildingUpdateView(UpdateView):
    # permission_required = ['movies.view_actor', 'movies.change_actor', ]
    model = Building
    fields = ("name", "description", "contract",)
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index_contracts")


class DrawingUpdateView(UpdateView):
    # permission_required = ['movies.view_actor', 'movies.change_actor', ]
    model = Drawing
    form_class = DrawingModelForm
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index_contracts")


# DELETEVIEW
class AddressDeleteView(DeleteView):
    # permission_required = ['movies.delete_actor', ]
    model = Address
    fields = ("street", "zip_code", "town",)
    template_name = "delete_form.html"
    success_url = reverse_lazy("contracts:index_contracts")


class CustomerDeleteView(DeleteView):
    # permission_required = ['movies.delete_actor', ]
    model = Customer
    fields = ("name", "description", "address",)
    template_name = "delete_form.html"
    success_url = reverse_lazy("contracts:index_contracts")


class RegionDeleteView(DeleteView):
    # permission_required = ['movies.delete_actor', ]
    model = Region
    fields = ("name", "prefix", "address",)
    template_name = "delete_form.html"
    success_url = reverse_lazy("contracts:index_contracts")


class PersonalDataDeleteView(DeleteView):
    # permission_required = ['movies.delete_actor', ]
    model = PersonalData
    fields = ("name", "last_name", "address",)
    template_name = "delete_form.html"
    success_url = reverse_lazy("contracts:index_contracts")


class DepartmentDeleteView(DeleteView):
    # permission_required = ['movies.delete_actor', ]
    model = Department
    fields = ("name", "description",)
    template_name = "delete_form.html"
    success_url = reverse_lazy("contracts:index_contracts")


class EmployeeDeleteView(DeleteView):
    # permission_required = ['movies.delete_actor', ]
    model = Employee
    fields = ("position", "hire_date", "personal_data", "department",)
    template_name = "delete_form.html"
    success_url = reverse_lazy("contracts:index_contracts")


class ContractDeleteView(DeleteView):
    # permission_required = ['movies.delete_actor', ]
    model = Contract
    form_class = ContractModelForm
    template_name = "delete_form.html"
    success_url = reverse_lazy("contracts:index_contracts")


class BuildingDeleteView(DeleteView):
    # permission_required = ['movies.delete_actor', ]
    model = Building
    fields = ("name", "description", "contract",)
    template_name = "delete_form.html"
    success_url = reverse_lazy("contracts:index_contracts")


class DrawingDeleteView(DeleteView):
    # permission_required = ['movies.delete_actor', ]
    model = Drawing
    form_class = DrawingModelForm
    template_name = "delete_form.html"
    success_url = reverse_lazy("contracts:index_contracts")
