from django import forms
from .models import Invoice


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['first_name', 'last_name', 'username', 'address', 'address2', 'total_amount']
