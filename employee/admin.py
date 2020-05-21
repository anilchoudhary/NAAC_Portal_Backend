from django.contrib import admin
from employee.models import EmployeeManager, Employee, DontFill

# Register your models here.

# admin.site.register(EmployeeManager)
admin.site.register(Employee)
admin.site.register(DontFill)
