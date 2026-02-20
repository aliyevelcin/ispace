from django import forms
from .models import *

class EmailForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'input-box', 'placeholder': 'E-mail'}),
        }