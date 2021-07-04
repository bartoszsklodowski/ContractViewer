from django.contrib import admin

from contracts.models import Address, Customer, Region, PersonalData, Department, Employee
from contracts.models import Contract, Building, Drawing


class AddressAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id', 'street', 'zip_code', 'town',)
    list_display_links = ('id',)
    list_per_page = 20
    list_filter = ('town',)
    search_fields = ('street', 'zip_code', 'town',)

    fieldsets = [
        ('General', {
            'fields': ['street', 'zip_code', 'town', ]
        }),
    ]


class CustomerAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id', 'name', 'description', 'address',)
    list_display_links = ('id',)
    list_per_page = 20
    list_filter = ('name',)
    search_fields = ('name', 'description', 'address',)
    actions = ('cleanup_description',)

    fieldsets = [
        ('General', {
            'fields': ['name', 'description', ]
        }),
        ('External Information', {
            'fields': ['address', ],
            'description': 'Information about related address'
        })
    ]

    @staticmethod
    def cleanup_description(modeladmin, request, queryset):
        queryset.update(description="")


class RegionAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id', 'name', 'prefix', 'address',)
    list_display_links = ('id',)
    list_per_page = 20
    list_filter = ('prefix',)
    search_fields = ('name', 'prefix', 'address',)

    fieldsets = [
        ('General', {
            'fields': ['name', 'prefix', ]
        }),
        ('External Information', {
            'fields': ['address', ],
            'description': 'Information about related address'
        })
    ]


class PersonalDataAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id', 'name', 'last_name', 'address',)
    list_display_links = ('id',)
    list_per_page = 20
    list_filter = ('last_name',)
    search_fields = ('name', 'last_name', 'address',)

    fieldsets = [
        ('General', {
            'fields': ['name', 'last_name', ]
        }),
        ('External Information', {
            'fields': ['address', ],
            'description': 'Information about related address'
        })
    ]


class DepartmentDataAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id', 'name', 'description',)
    list_display_links = ('id',)
    list_per_page = 20
    list_filter = ('name',)
    search_fields = ('name', 'description',)

    fieldsets = [
        ('General', {
            'fields': ['name', 'description', ]
        }),
    ]


class EmployeeDataAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id', 'position', 'hire_date', 'personal_data', 'department',)
    list_display_links = ('id',)
    list_per_page = 20
    list_filter = ('personal_data',)
    search_fields = ('position', 'hire_date', 'personal_data', 'department',)

    fieldsets = [
        ('General', {
            'fields': ['position', 'hire_date', ]
        }),
        ('External Information', {
            'fields': ['personal_data', 'department', ],
            'description': 'Information about related personal data and department'
        })
    ]


class ContractAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = (
        'id', 'number', 'name', 'type', 'start_date', 'end_date', 'description', 'address', 'customer', 'region',
        'employees',)
    list_display_links = ('id',)
    list_per_page = 20
    list_filter = ('number',)
    search_fields = ('number', 'name', 'type',)
    actions = ('cleanup_description',)

    fieldsets = [
        ('General', {
            'fields': ['number', 'name', 'type', 'start_date', 'end_date', 'description', ]
        }),
        ('External Information', {
            'fields': ['address', 'customer', 'region', 'employee', ],
            'description': 'Information about related address, customer, region and employee'
        })
    ]

    def employees(self, obj):
        queryset = Employee.objects.filter(contracts__number=obj.number)
        if queryset:
            employees = [(x.position, x.personal_data.name, x.personal_data.last_name) for x in queryset]
            return f'{employees}'

    @staticmethod
    def cleanup_description(modeladmin, request, queryset):
        queryset.update(description="")


class BuildingAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id', 'name', 'description', 'contract',)
    list_display_links = ('id',)
    list_per_page = 20
    list_filter = ('name', 'contract',)
    search_fields = ('name', 'description', 'contract',)
    actions = ('cleanup_description',)

    fieldsets = [
        ('General', {
            'fields': ['name', 'description', ]
        }),
        ('External Information', {
            'fields': ['contract', ],
            'description': 'Information about related contract'
        })
    ]

    @staticmethod
    def cleanup_description(modeladmin, request, queryset):
        queryset.update(description="")


class DrawingAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = (
        'id', 'number', 'element', 'revision', 'creation_date', 'modification_date', 'technician', 'building',
        'contract',)
    list_display_links = ('id',)
    list_per_page = 20
    list_filter = ('number',)
    search_fields = ('number', 'element', 'revision',)

    fieldsets = [
        ('General', {
            'fields': ['number', 'element', 'revision', 'creation_date', 'modification_date', ]
        }),
        ('External Information', {
            'fields': ['technician', 'building', 'contract', ],
            'description': 'Information about related technician, building, contract'
        })
    ]

    readonly_fields = ['creation_date']


admin.site.register(Address, AddressAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(PersonalData, PersonalDataAdmin)
admin.site.register(Department, DepartmentDataAdmin)
admin.site.register(Employee, EmployeeDataAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Drawing, DrawingAdmin)
