from django.db import models


class Employee(models.Model):
    uuid = models.UUIDField()
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)

    def __str__(self):
        return str(self.uuid)


class Expense(models.Model):
    uuid = models.UUIDField()
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField()
    amount = models.IntegerField()
    currency = models.CharField(max_length=100)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

