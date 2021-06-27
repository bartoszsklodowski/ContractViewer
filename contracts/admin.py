from django.contrib import admin

from contracts.models import Address, Customer, Region, PersonalData, Department, Employee
from contracts.models import Contract, Building, Drawing

admin.site.register(Address)
admin.site.register(Customer)
admin.site.register(Region)
admin.site.register(PersonalData)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Contract)
admin.site.register(Building)
admin.site.register(Drawing)

