from django import forms
from .models import Demand
class FulfillDemandForm(forms.ModelForm):
    class Meta:
        model= Demand
        fields= ('f_content',)
        labels = {
            'f_content': ('File Upload'),
        }