from django import forms
from .models import TicketBook


class TicketForm(forms.ModelForm):
    class Meta:
        model = TicketBook
        fields = '__all__'

        widgets = {
            "ticket_no": forms.NumberInput(attrs={'class': 'form-control'}),
            "from_place": forms.TextInput(attrs={'class': 'form-control'}),
            "destination": forms.TextInput(attrs={'class': 'form-control'}),
            "travelling_date": forms.TextInput(attrs={'class': 'form-control'}),
            "bus_type": forms.TextInput(attrs={'class': 'form-control'}),
            "amount": forms.NumberInput(attrs={'class': 'form-control'}),
        }

