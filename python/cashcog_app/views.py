import logging
import requests
from django.conf import settings
from django.db.models import Q
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from cashcog_app.models import Expense, Employee
from cashcog_app.serializers.expense import ExpenseSerializer

logger = logging.getLogger(__name__)


def get_expense_data(expense_data):
    data = ExpenseSerializer(expense_data).data
    return data


class DataExpenseAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        datas = []
        try:
            all_data = Expense.objects.all()
            if all_data is not None:
                for expense_data in all_data:
                    result = get_expense_data(expense_data)
                    datas.append(result)
                return Response({'res': datas})
            else:
                return Response({'message': 'No records found!'}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.exception('Error while getting expense data: {}'.format(ex))

    def post(self, request):
        expense_api_url = settings.CASHCOG_EXPENSE_API_URL
        try:
            res = requests.get(expense_api_url)
            data = res.json()

            employee_data_store = Employee.objects.update_or_create(
                uuid=data['employee']['uuid'],
                first_name=data['employee']['first_name'],
                last_name=data['employee']['last_name']
            )
            employee_data_store.save()
            expense_data_store = Expense.objects.update_or_create(
                uuid=data['uuid'],
                description=data['description'],
                created_at=data['created_at'],
                amount=data['amount'],
                currency=data['currency'],
                employee=employee_data_store[0]
            )
            expense_data_store.save()
            return Response({'success': 'Expenses added/updated successfully!'}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.exception('Error while inserting/updating expense data: {}'.format(ex))


class FilterExpenseAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = request.query_params.get('query')
        datas = []
        try:
            filter_data = Expense.objects.filter(Q(uuid__exact=query) or Q(amount__exact=int(query)) or
                                                 Q(currency__exact=query) or Q(employee__uuid__exact=query) or
                                                 Q(employee__first_name__exact=query) or
                                                 Q(employee__last_name__exact=query))
            if filter_data is not None:
                for expense_data in filter_data:
                    result = get_expense_data(expense_data)
                    datas.append(result)
                return Response({'res': datas})
            else:
                return Response({'message': 'No records found!'}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.exception('Error while filtering expense data: {}'.format(ex))
