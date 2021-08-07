from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from contracts.models import Address, Customer, Region, PersonalData, Department, Employee, Contract, Building, Drawing
from contracts.forms import AddressModelForm, CustomerModelForm, RegionModelForm, PersonalDataModelForm, \
    DepartmentModelForm
from contracts.forms import EmployeeModelForm, ContractModelForm, BuildingModelForm, DrawingModelForm
from contracts.filters import AddressFilter, CustomerFilter, RegionFilter, PersonalDataFilter, DepartmentFilter
from contracts.filters import EmployeeFilter, ContractFilter, BuildingFilter, DrawingFilter


@login_required(login_url="/accounts/login/")
def insert_data(request):
    return render(request, template_name="insert_data.html")


def homepage(request):
    return render(request, template_name="homepage.html")


@login_required(login_url="/accounts/login/")
def index_contracts(request):
    return render(request, template_name="index_contracts.html")


@login_required(login_url="/accounts/login/")
def contract_multiple_view(request):
    contracts = Contract.objects.all().order_by('name')
    return render(request, template_name='contracts_view.html',
                  context={'contracts': contracts, })


# LISTVIEW
class AddressListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = ['contracts.view_address', ]
    template_name = "addresses.html"
    model = Address
    ordering = ['town']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = AddressFilter(self.request.GET, queryset=self.get_queryset())
        return context


class CustomerListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = ['contracts.view_customer', ]
    template_name = "customers.html"
    model = Customer
    ordering = ['name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CustomerFilter(self.request.GET, queryset=self.get_queryset())
        return context


class RegionListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = ['contracts.view_region', ]
    template_name = "regions.html"
    model = Region
    ordering = ['prefix']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = RegionFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PersonalDataListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = ['contracts.view_personal_data', ]
    template_name = "personal_datas.html"
    model = PersonalData
    ordering = ['last_name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PersonalDataFilter(self.request.GET, queryset=self.get_queryset())
        return context


class DepartmentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = ['contracts.view_department', ]
    template_name = "departments.html"
    model = Department
    ordering = ['name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = DepartmentFilter(self.request.GET, queryset=self.get_queryset())
        return context


class EmployeeListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = ['contracts.view_employee', ]
    template_name = "employees.html"
    model = Employee
    ordering = ['personal_data__last_name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = EmployeeFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ContractListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = ['contracts.view_contract', ]
    template_name = "contracts.html"
    model = Contract
    ordering = ['number']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ContractFilter(self.request.GET, queryset=self.get_queryset())
        return context


class BuildingListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = ['contracts.view_building', ]
    template_name = "buildings.html"
    model = Building
    ordering = ['name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = BuildingFilter(self.request.GET, queryset=self.get_queryset())
        return context


class DrawingListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = ['contracts.view_drawing', ]
    template_name = "drawings.html"
    model = Drawing
    ordering = ['building', 'number']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = DrawingFilter(self.request.GET, queryset=self.get_queryset())
        return context


# DETAILVIEW
class AddressDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = ['contracts.view_address', ]
    model = Address
    template_name = "address.html"


class CustomerDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = ['contracts.view_customer', ]
    model = Customer
    template_name = "customer.html"


class RegionDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = ['contracts.view_region', ]
    model = Region
    template_name = "region.html"


class PersonalDataDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = ['contracts.view_personal_data', ]
    model = PersonalData
    template_name = "personal_data.html"


class DepartmentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = ['contracts.view_department', ]
    model = Department
    template_name = "department.html"


class EmployeeDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = ['contracts.view_employee', ]
    model = Employee
    template_name = "employee.html"


class ContractDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = ['contracts.view_contract', ]
    model = Contract
    template_name = "contract.html"


class BuildingDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = ['contracts.view_building', ]
    model = Building
    template_name = "building.html"


class DrawingDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = ['contracts.view_drawing', ]
    model = Drawing
    template_name = "drawing.html"


# CREATEVIEW
class AddressCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ['contracts.add_address', ]
    model = Address
    form_class = AddressModelForm
    template_name = "form.html"
    success_url = reverse_lazy("contracts:insert_data")


class CustomerCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ['contracts.add_customer', ]
    model = Customer
    form_class = CustomerModelForm
    template_name = "form.html"
    success_url = reverse_lazy("contracts:insert_data")


class RegionCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ['contracts.add_region', ]
    model = Region
    form_class = RegionModelForm
    template_name = "form.html"
    success_url = reverse_lazy("contracts:insert_data")


class PersonalDataCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ['contracts.add_personal_data', ]
    model = PersonalData
    form_class = PersonalDataModelForm
    template_name = "form.html"
    success_url = reverse_lazy("contracts:insert_data")


class DepartmentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ['contracts.add_department', ]
    model = Department
    form_class = DepartmentModelForm
    template_name = "form.html"
    success_url = reverse_lazy("contracts:insert_data")


class EmployeeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ['contracts.add_employee', ]
    model = Employee
    form_class = EmployeeModelForm
    template_name = "form.html"
    success_url = reverse_lazy("contracts:insert_data")


class ContractCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ['contracts.add_contract', ]
    model = Contract
    form_class = ContractModelForm
    template_name = "form.html"
    success_url = reverse_lazy("contracts:insert_data")


class BuildingCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ['contracts.add_building', ]
    model = Building
    form_class = BuildingModelForm
    template_name = "form.html"
    success_url = reverse_lazy("contracts:insert_data")


class DrawingCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ['contracts.add_drawing', ]
    model = Drawing
    form_class = DrawingModelForm
    template_name = "form.html"
    success_url = reverse_lazy("contracts:insert_data")


# UPDATEVIEW
class AddressUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ['contracts.view_address', 'contracts.change_address', ]
    model = Address
    fields = ("street", "zip_code", "town",)
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index")


class CustomerUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ['contracts.view_customer', 'contracts.change_customer', ]
    model = Customer
    fields = ("name", "description", "address",)
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index")


class RegionUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ['contracts.view_region', 'contracts.change_region']
    model = Region
    fields = ("name", "prefix", "address",)
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index")


class PersonalDataUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ['contracts.view_personal_data', 'contracts.change_personal_data', ]
    model = PersonalData
    fields = ("name", "last_name", "address",)
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index")


class DepartmentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ['contracts.view_department', 'contracts.change_department', ]
    model = Department
    fields = ("name", "description",)
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index")


class EmployeeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ['contracts.view_employee', 'contracts.change_employee', ]
    model = Employee
    fields = ("position", "hire_date", "personal_data", "department",)
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index")


class ContractUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ['contracts.view_contract', 'contracts.change_contract', ]
    model = Contract
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index")


class BuildingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ['contracts.view_building', 'contracts.change_building', ]
    model = Building
    fields = ("name", "description", "contract",)
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index")


class DrawingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ['contracts.view_drawing', 'contracts.change_drawing', ]
    model = Drawing
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index")


# DELETEVIEW
class AddressDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ['contracts.delete_address', ]
    model = Address
    template_name = "delete_form.html"
    success_url = reverse_lazy("contracts:index")


class CustomerDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ['contracts.delete_customer', ]
    model = Customer
    template_name = "delete_form.html"
    success_url = reverse_lazy("contracts:index")


class RegionDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ['contracts.delete_region', ]
    model = Region
    template_name = "delete_form.html"
    success_url = reverse_lazy("contracts:index")


class PersonalDataDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ['contracts.delete_personal_data', ]
    model = PersonalData
    template_name = "delete_form.html"
    success_url = reverse_lazy("contracts:index")


class DepartmentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ['contracts.delete_department', ]
    model = Department
    template_name = "delete_form.html"
    success_url = reverse_lazy("contracts:index")


class EmployeeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ['contracts.delete_employee', ]
    model = Employee
    template_name = "delete_form.html"
    success_url = reverse_lazy("contracts:index")


class ContractDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ['contracts.delete_contract', ]
    model = Contract
    template_name = "delete_form.html"
    success_url = reverse_lazy("contracts:index")


class BuildingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ['contracts.delete_building', ]
    model = Building
    template_name = "delete_form.html"
    success_url = reverse_lazy("contracts:index")


class DrawingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ['contracts.delete_drawing', ]
    model = Drawing
    template_name = "delete_form.html"
    success_url = reverse_lazy("contracts:index")


class ContractSearchView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = ['contracts.view_contract', ]
    template_name = "search_contracts.html"
    model = Contract
    ordering = ['number']

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = Contract.objects.filter(
                Q(number__icontains=query) | Q(name__icontains=query) | Q(type__icontains=query) |
                Q(address__street__icontains=query) | Q(address__zip_code__icontains=query) | Q(
                    address__town__icontains=query)
                | Q(customer__name__icontains=query) | Q(region__name__icontains=query) |
                Q(employee__personal_data__name__icontains=query) | Q(employee__personal_data__last_name__icontains=query)
            ).distinct()
            return object_list
        return []
