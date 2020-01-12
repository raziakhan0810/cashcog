from rest_framework import serializers

from cashcog_app.models import Expense, Employee


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('uuid', 'first_name', 'last_name')


class ExpenseSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()

    class Meta:
        model = Expense
        fields = ('uuid', 'description', 'created_at', 'amount', 'currency', 'employee')
