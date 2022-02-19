from django.db.models import F
from django.db import transaction
from rest_framework import status, views
from rest_framework.response import Response as response
from rest_framework.decorators import action
from datetime import datetime
from .serializers import AccountDetailsSerializer
from .models import AccountDetails


class TransactionsView(views.APIView):

    def get(self, request, date):
        date = datetime.strptime(date, "%-d-%m-%y")
        data = AccountDetails.objects.filter(date=date).values()
        return response({"data":data},status=status.HTTP_200_OK)
    
    def retrieve(self, request, id):
        data = AccountDetails.objects.filter(id=id).values()
        return response({"data":data},status=status.HTTP_200_OK)


class BalanceView(views.APIView):

    def get(self, request, date):
        date = datetime.strptime(date, "%-d-%m-%y")
        data = AccountDetails.objects.filter(date__lte=date).values('balance_amt').last()
        return response({"data":data},status=status.HTTP_200_OK)
    
    @transaction.atomic
    def post(self, request):
        acnt_no = request.data.get('Account No')
        date = request.data.get('Date')
        txn_dtls = request.data.get('Transaction Details')
        value_date = request.data.get('Value Date')
        withdrawal_amt = request.data.get('Withdrawal AMT')
        deposit_amt = request.data.get('Deposit AMT')
        balance_amt = request.data.get('Balance AMT')

        date = datetime.strptime(date, "%-d %b %y")
        value_date = datetime.strptime(date, "%-d %b %y")

        serializer = AccountDetailsSerializer(data={"acnt_no":acnt_no, "date":date, "txn_dtls":txn_dtls, "value_date":value_date, "withdrawal_amt":withdrawal_amt, "deposit_amt":deposit_amt, "balance_amt":balance_amt})
        if not serializer.is_valid():
            return response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        data = serializer.validated_data
        AccountDetails.objects.create(anct_no=data['acnt_no'], txn_dtls=data['txn_dtls'], date=data['date'], value_date=data['value_date'], withdrawal_amt=data['withdrawal_amt'], deposit_amt=data['deposit_amt'], balance_amt=data['balance_amt'])
        return response({"msg": "Created Successfully"},status=status.HTTP_201_CREATED)

