from datetime import datetime
from rest_framework import serializers

class AccountDetailsSerializer(serializers.Serializer):

    anct_no = serializers.IntegerField(required=True)
    date = serializers.DateTimeField(required=True)
    txn_dtls = serializers.CharField(required=True)
    value_date = serializers.DateTimeField
    withdrawal_amt = serializers.DecimalField(required=True, max_digits=19, decimal_places=2)
    deposit_amt = serializers.DecimalField(required=True, max_digits=19, decimal_places=2)
    balance_amt = serializers.DecimalField(required=True, max_digits=19, decimal_places=2)

    def validate(self, data):

        if data['date'].date() < datetime.now().date():
            raise serializers.ValidationError('Date/Value Date cannot be in future')
        return data

    class Meta:
        fields = '__all__'