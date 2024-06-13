from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    """
    Model representing a transaction.
    """
    TRANSACTION_TYPES = [
        ('KIRIM', 'Kirim'),
        ('CHIQIM', 'Chiqim'),
    ]

    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=50, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
                String representation of the transaction.
        """
        return f"{self.transaction_type} - {self.amount}"
