from django.contrib import admin

from cashcog_app.models import Employee, Expense


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'first_name', 'last_name')


@admin.register(Expense)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'description', 'created_at', 'amount', 'currency', 'employee')
