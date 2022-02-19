from django.db import models


class AccountDetails(models.Model):
    id = models.IntegerField(primary_key=True)
    anct_no = models.IntegerField()
    date = models.DateTimeField()
    txn_dtls = models.CharField(max_length=100)
    value_date = models.DateTimeField()
    withdrawal_amt = models.DecimalField(max_digits=19, decimal_places=2)
    deposit_amt = models.DecimalField(max_digits=19, decimal_places=2)
    balance_amt = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        db_table = 'account_details'
