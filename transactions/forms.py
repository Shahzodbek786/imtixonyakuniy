from django import forms
from django.contrib.auth.models import User
from .models import Transaction

class TransactionForm(forms.ModelForm):
    """
    Form for creating or updating a transaction.
    Uses Transaction model to define fields.
    Attributes:
    amount (decimal): Amount of the transaction.
    transaction_type (str): Type of the transaction (KIRIM or CHIQIM).
    """
    class Meta:
        """
        Meta class defining model and fields.
        """
        model = Transaction
        fields = ['amount', 'transaction_type']