from django.db import models


# Create your models here.

class Address(models.Model):

    street = models.CharField(max_length=128)
    zip_code = models.CharField(max_length=6)
    town = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.street} {self.zip_code} {self.town}"


class Customer(models.Model):

    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="customers")

    def __str__(self):
        return f"{self.name} {self.description} {self.address}"


class Region(models.Model):

    name = models.CharField(max_length=30)
    prefix = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="regions")

    def __str__(self):
        return f"{self.name} {self.prefix} {self.address}"


class PersonalData(models.Model):

    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=48)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="personal_data")

    def __str__(self):
        return f"{self.name} {self.last_name} {self.address}"


class Department(models.Model):

    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.description}"


class Employee(models.Model):

    position = models.CharField(max_length=30)
    hire_date = models.DateField()
    personal_data = models.ForeignKey(PersonalData, on_delete=models.CASCADE, related_name="employees")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="employees")

    class Meta:
        ordering = ['position', 'hire_date']

    def __str__(self):
        return f"{self.position} {self.personal_data.name} {self.personal_data.last_name} {self.department}"


class Contract(models.Model):

    number = models.CharField(max_length=10)
    name = models.CharField(max_length=40)
    type = models.CharField(max_length=40)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True, related_name="contracts")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="contracts")
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="contracts")
    employee = models.ManyToManyField(Employee, blank=True, related_name="contracts")

    class Meta:
        ordering = ['number', 'name', 'type', 'start_date', 'end_date']

    def __str__(self):
        return f"{self.number} {self.name}"


class Building(models.Model):

    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, null=True, related_name="buildings")

    def __str__(self):
        return f"{self.name} {self.description}"


class Drawing(models.Model):

    number = models.CharField(max_length=15)
    element = models.CharField(max_length=40, blank=True)
    revision = models.CharField(max_length=1, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(null=True, blank=True)
    technician = models.ForeignKey(Employee, on_delete=models.CASCADE,related_name="drawings")
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name="drawings")
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name="drawings")

    def __str__(self):
        return f"{self.number} {self.element} {self.revision} {self.creation_date} {self.modification_date}"
