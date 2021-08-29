from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import request, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django_filters.views import FilterView

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
    contracts = Contract.objects.all().order_by('number')
    paginator = Paginator(contracts, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, template_name='contracts_view.html',
                  context={'contracts': page_obj, })


# FILTERVIEW(LISTVIEW)
class AddressListView(LoginRequiredMixin, PermissionRequiredMixin, FilterView):
    permission_required = ['contracts.view_address', ]
    template_name = "addresses.html"
    model = Address
    paginate_by = 15
    ordering = ['town']
    filterset_class = AddressFilter


class CustomerListView(LoginRequiredMixin, PermissionRequiredMixin, FilterView):
    permission_required = ['contracts.view_customer', ]
    template_name = "customers.html"
    model = Customer
    ordering = ['name']
    paginate_by = 15
    filterset_class = CustomerFilter


class RegionListView(LoginRequiredMixin, PermissionRequiredMixin, FilterView):
    permission_required = ['contracts.view_region', ]
    template_name = "regions.html"
    model = Region
    ordering = ['prefix']
    paginate_by = 15
    filterset_class = RegionFilter


class PersonalDataListView(LoginRequiredMixin, PermissionRequiredMixin, FilterView):
    permission_required = ['contracts.view_personal_data', ]
    template_name = "personal_datas.html"
    model = PersonalData
    ordering = ['last_name']
    paginate_by = 15
    filterset_class = PersonalDataFilter


class DepartmentListView(LoginRequiredMixin, PermissionRequiredMixin, FilterView):
    permission_required = ['contracts.view_department', ]
    template_name = "departments.html"
    model = Department
    ordering = ['name']
    paginate_by = 15
    filterset_class = DepartmentFilter


class EmployeeListView(LoginRequiredMixin, PermissionRequiredMixin, FilterView):
    permission_required = ['contracts.view_employee', ]
    template_name = "employees.html"
    model = Employee
    ordering = ['personal_data__last_name']
    paginate_by = 15
    filterset_class = EmployeeFilter


class ContractListView(LoginRequiredMixin, PermissionRequiredMixin, FilterView):
    permission_required = ['contracts.view_contract', ]
    template_name = "contracts.html"
    model = Contract
    ordering = ['number']
    paginate_by = 15
    filterset_class = ContractFilter


class BuildingListView(LoginRequiredMixin, PermissionRequiredMixin, FilterView):
    permission_required = ['contracts.view_building', ]
    template_name = "buildings.html"
    model = Building
    ordering = ['name']
    paginate_by = 15
    filterset_class = BuildingFilter


class DrawingListView(LoginRequiredMixin, PermissionRequiredMixin, FilterView):
    permission_required = ['contracts.view_drawing', ]
    template_name = "drawings.html"
    model = Drawing
    ordering = ['building', 'number']
    paginate_by = 15
    filterset_class = DrawingFilter


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

    def form_valid(self, form):
        messages.success(self.request, "Address created successfully")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


class CustomerCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ['contracts.add_customer', ]
    model = Customer
    form_class = CustomerModelForm
    template_name = "form.html"
    success_url = reverse_lazy("contracts:insert_data")

    def form_valid(self, form):
        messages.success(self.request, "Customer created successfully")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


class RegionCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ['contracts.add_region', ]
    model = Region
    form_class = RegionModelForm
    template_name = "form.html"
    success_url = reverse_lazy("contracts:insert_data")

    def form_valid(self, form):
        messages.success(self.request, "Region created successfully")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


class PersonalDataCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ['contracts.add_personal_data', ]
    model = PersonalData
    form_class = PersonalDataModelForm
    template_name = "form.html"
    success_url = reverse_lazy("contracts:insert_data")

    def form_valid(self, form):
        messages.success(self.request, "Personal data created successfully")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


class DepartmentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ['contracts.add_department', ]
    model = Department
    form_class = DepartmentModelForm
    template_name = "form.html"
    success_url = reverse_lazy("contracts:insert_data")

    def form_valid(self, form):
        messages.success(self.request, "Department created successfully")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


class EmployeeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ['contracts.add_employee', ]
    model = Employee
    form_class = EmployeeModelForm
    template_name = "form.html"
    success_url = reverse_lazy("contracts:insert_data")

    def form_valid(self, form):
        messages.success(self.request, "Employee created successfully")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


class ContractCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ['contracts.add_contract', ]
    model = Contract
    form_class = ContractModelForm
    template_name = "form.html"
    success_url = reverse_lazy("contracts:insert_data")

    def form_valid(self, form):
        messages.success(self.request, "Contract created successfully")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


class BuildingCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ['contracts.add_building', ]
    model = Building
    form_class = BuildingModelForm
    template_name = "form.html"
    success_url = reverse_lazy("contracts:insert_data")

    def form_valid(self, form):
        messages.success(self.request, "Building created successfully")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


class DrawingCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ['contracts.add_drawing', ]
    model = Drawing
    form_class = DrawingModelForm
    template_name = "form.html"
    success_url = reverse_lazy("contracts:insert_data")

    def form_valid(self, form):
        messages.success(self.request, "Drawing created successfully")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


# UPDATEVIEW
class AddressUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ['contracts.view_address', 'contracts.change_address', ]
    model = Address
    fields = ("street", "zip_code", "town",)
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index")

    def form_valid(self, form):
        messages.success(self.request, "Address updated successfully")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


class CustomerUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ['contracts.view_customer', 'contracts.change_customer', ]
    model = Customer
    fields = ("name", "description", "address",)
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index")

    def form_valid(self, form):
        messages.success(self.request, "Customer updated successfully")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


class RegionUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ['contracts.view_region', 'contracts.change_region']
    model = Region
    fields = ("name", "prefix", "address",)
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index")

    def form_valid(self, form):
        messages.success(self.request, "Region updated successfully")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


class PersonalDataUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ['contracts.view_personal_data', 'contracts.change_personal_data', ]
    model = PersonalData
    fields = ("name", "last_name", "address",)
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index")

    def form_valid(self, form):
        messages.success(self.request, "Personal data updated successfully")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


class DepartmentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ['contracts.view_department', 'contracts.change_department', ]
    model = Department
    fields = ("name", "description",)
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index")

    def form_valid(self, form):
        messages.success(self.request, "Department updated successfully")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


class EmployeeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ['contracts.view_employee', 'contracts.change_employee', ]
    model = Employee
    fields = ("position", "hire_date", "personal_data", "department",)
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index")

    def form_valid(self, form):
        messages.success(self.request, "Employee updated successfully")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


class ContractUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ['contracts.view_contract', 'contracts.change_contract', ]
    model = Contract
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index")

    def form_valid(self, form):
        messages.success(self.request, "Contract updated successfully")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


class BuildingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ['contracts.view_building', 'contracts.change_building', ]
    model = Building
    fields = ("name", "description", "contract",)
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index")

    def form_valid(self, form):
        messages.success(self.request, "Building updated successfully")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


class DrawingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ['contracts.view_drawing', 'contracts.change_drawing', ]
    model = Drawing
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("contracts:index")

    def form_valid(self, form):
        messages.success(self.request, "Drawing updated successfully")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


# DELETEVIEW
class AddressDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ['contracts.delete_address', ]
    model = Address
    template_name = "delete_form.html"
    success_url = reverse_lazy("contracts:index")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Address deleted successfully")
        return super(AddressDeleteView, self).delete(request, *args, **kwargs)


class CustomerDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ['contracts.delete_customer', ]
    model = Customer
    template_name = "delete_form.html"
    success_url = reverse_lazy("contracts:index")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Customer deleted successfully")
        return super(CustomerDeleteView, self).delete(request, *args, **kwargs)


class RegionDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ['contracts.delete_region', ]
    model = Region
    template_name = "delete_form.html"
    success_url = reverse_lazy("contracts:index")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Region deleted successfully")
        return super(RegionDeleteView, self).delete(request, *args, **kwargs)


class PersonalDataDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ['contracts.delete_personal_data', ]
    model = PersonalData
    template_name = "delete_form.html"
    success_url = reverse_lazy("contracts:index")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Personal data deleted successfully")
        return super(PersonalDataDeleteView, self).delete(request, *args, **kwargs)


class DepartmentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ['contracts.delete_department', ]
    model = Department
    template_name = "delete_form.html"
    success_url = reverse_lazy("contracts:index")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Department deleted successfully")
        return super(DepartmentDeleteView, self).delete(request, *args, **kwargs)


class EmployeeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ['contracts.delete_employee', ]
    model = Employee
    template_name = "delete_form.html"
    success_url = reverse_lazy("contracts:index")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Employee deleted successfully")
        return super(EmployeeDeleteView, self).delete(request, *args, **kwargs)


class ContractDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ['contracts.delete_contract', ]
    model = Contract
    template_name = "delete_form.html"
    success_url = reverse_lazy("contracts:index")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Contract deleted successfully")
        return super(ContractDeleteView, self).delete(request, *args, **kwargs)


class BuildingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ['contracts.delete_building', ]
    model = Building
    template_name = "delete_form.html"
    success_url = reverse_lazy("contracts:index")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Building deleted successfully")
        return super(BuildingDeleteView, self).delete(request, *args, **kwargs)


class DrawingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ['contracts.delete_drawing', ]
    model = Drawing
    template_name = "delete_form.html"
    success_url = reverse_lazy("contracts:index")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Drawing deleted successfully")
        return super(DrawingDeleteView, self).delete(request, *args, **kwargs)


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
                Q(employee__personal_data__name__icontains=query) | Q(
                    employee__personal_data__last_name__icontains=query)
            ).distinct()
            return object_list
        return []


# PDF VIEWS
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders


def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    result = finders.find(uri)
    if result:
        if not isinstance(result, (list, tuple)):
            result = [result]
        result = list(os.path.realpath(path) for path in result)
        path = result[0]
    else:
        sUrl = settings.STATIC_URL  # Typically /static/
        sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL  # Typically /media/
        mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri

    # make sure that file exists
    if not os.path.isfile(path):
        raise Exception(
            'media URI must start with %s or %s' % (sUrl, mUrl)
        )
    return path


def contracts_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    contract = get_object_or_404(Contract, pk=pk)
    buildings = Building.objects.filter(contract__number=contract.number)

    template_path = 'contracts_pdf.html'
    context = {'contract': contract, 'buildings': buildings}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

