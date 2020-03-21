from django import forms
from .models import FulfillContent
class FulfillDemandForm(forms.Form):
    f_suggestion= forms.CharField(label="Suggestions (if any)" ,required=False,widget=forms.Textarea(attrs={"rows":4, "cols":70}))
    f_content=forms.FileField(label="Upload Content ",required=False)
