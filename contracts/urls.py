from django.urls import path
from contracts.views import index_contracts, AddressListView, CustomerListView, RegionListView, PersonalDataListView
from contracts.views import DepartmentListView, EmployeeListView, ContractListView, BuildingListView, DrawingListView
from contracts.views import AddressDetailView, CustomerDetailView, RegionDetailView, PersonalDataDetailView
from contracts.views import DepartmentDetailView, EmployeeDetailView, ContractDetailView, BuildingDetailView
from contracts.views import DrawingDetailView
from contracts.views import AddressCreateView, CustomerCreateView, RegionCreateView, PersonalDataCreateView
from contracts.views import DepartmentCreateView, EmployeeCreateView, ContractCreateView, BuildingCreateView
from contracts.views import DrawingCreateView
from contracts.views import AddressUpdateView, CustomerUpdateView, RegionUpdateView, PersonalDataUpdateView
from contracts.views import DepartmentUpdateView, EmployeeUpdateView, ContractUpdateView, BuildingUpdateView
from contracts.views import DrawingUpdateView
from contracts.views import AddressDeleteView, CustomerDeleteView, RegionDeleteView, PersonalDataDeleteView
from contracts.views import DepartmentDeleteView, EmployeeDeleteView, ContractDeleteView, BuildingDeleteView
from contracts.views import DrawingDeleteView, insert_data, homepage, contract_multiple_view
from contracts.views import contracts_render_pdf_view

app_name = "contracts"

urlpatterns = [
    path('', homepage, name='homepage'),
    path('insert_data/', insert_data, name='insert_data'),
    path('index/', index_contracts, name='index'),

    path('addresses/', AddressListView.as_view(), name='addresses'),
    path('customers/', CustomerListView.as_view(), name='customers'),
    path('regions/', RegionListView.as_view(), name='regions'),
    path('personal_datas/', PersonalDataListView.as_view(), name='personal_datas'),
    path('departments/', DepartmentListView.as_view(), name='departments'),
    path('employees/', EmployeeListView.as_view(), name='employees'),
    path('contracts/', ContractListView.as_view(), name='contracts'),
    path('buildings/', BuildingListView.as_view(), name='buildings'),
    path('drawings/', DrawingListView.as_view(), name='drawings'),

    path('address-detail-view/<pk>/', AddressDetailView.as_view(), name='address-detail-view'),
    path('customer-detail-view/<pk>/', CustomerDetailView.as_view(), name='customer-detail-view'),
    path('region-detail-view/<pk>/', RegionDetailView.as_view(), name='region-detail-view'),
    path('personal_data-detail-view/<pk>/', PersonalDataDetailView.as_view(), name='personal_data-detail-view'),
    path('department-detail-view/<pk>/', DepartmentDetailView.as_view(), name='department-detail-view'),
    path('employee-detail-view/<pk>/', EmployeeDetailView.as_view(), name='employee-detail-view'),
    path('contract-detail-view/<pk>/', ContractDetailView.as_view(), name='contract-detail-view'),
    path('building-detail-view/<pk>/', BuildingDetailView.as_view(), name='building-detail-view'),
    path('drawing-detail-view/<pk>/', DrawingDetailView.as_view(), name='drawing-detail-view'),

    path('address-create-view/', AddressCreateView.as_view(), name='address-create-view'),
    path('customer-create-view/', CustomerCreateView.as_view(), name='customer-create-view'),
    path('region-create-view/', RegionCreateView.as_view(), name='region-create-view'),
    path('personal_data-create-view/', PersonalDataCreateView.as_view(), name='personal_data-create-view'),
    path('department-create-view/', DepartmentCreateView.as_view(), name='department-create-view'),
    path('employee-create-view/', EmployeeCreateView.as_view(), name='employee-create-view'),
    path('contract-create-view/', ContractCreateView.as_view(), name='contract-create-view'),
    path('building-create-view/', BuildingCreateView.as_view(), name='building-create-view'),
    path('drawing-create-view/', DrawingCreateView.as_view(), name='drawing-create-view'),

    path('address-update-view/<pk>/', AddressUpdateView.as_view(), name='address-update-view'),
    path('customer-update-view/<pk>/', CustomerUpdateView.as_view(), name='customer-update-view'),
    path('region-update-view/<pk>/', RegionUpdateView.as_view(), name='region-update-view'),
    path('personal_data-update-view/<pk>/', PersonalDataUpdateView.as_view(), name='personal_data-update-view'),
    path('department-update-view/<pk>/', DepartmentUpdateView.as_view(), name='department-update-view'),
    path('employee-update-view/<pk>/', EmployeeUpdateView.as_view(), name='employee-update-view'),
    path('contract-update-view/<pk>/', ContractUpdateView.as_view(), name='contract-update-view'),
    path('building-update-view/<pk>/', BuildingUpdateView.as_view(), name='building-update-view'),
    path('drawing-update-view/<pk>/', DrawingUpdateView.as_view(), name='drawing-update-view'),

    path('address-delete-view/<pk>/', AddressDeleteView.as_view(), name='address-delete-view'),
    path('customer-delete-view/<pk>/', CustomerDeleteView.as_view(), name='customer-delete-view'),
    path('region-delete-view/<pk>/', RegionDeleteView.as_view(), name='region-delete-view'),
    path('personal_data-delete-view/<pk>/', PersonalDataDeleteView.as_view(), name='personal_data-delete-view'),
    path('department-delete-view/<pk>/', DepartmentDeleteView.as_view(), name='department-delete-view'),
    path('employee-delete-view/<pk>/', EmployeeDeleteView.as_view(), name='employee-delete-view'),
    path('contract-delete-view/<pk>/', ContractDeleteView.as_view(), name='contract-delete-view'),
    path('building-delete-view/<pk>/', BuildingDeleteView.as_view(), name='building-delete-view'),
    path('drawing-delete-view/<pk>/', DrawingDeleteView.as_view(), name='drawing-delete-view'),

    path('contract-multiple-view/', contract_multiple_view, name='contract-multiple-view'),

    path('contracts-pdf/<pk>/', contracts_render_pdf_view, name='contracts-pdf-view'),

]
