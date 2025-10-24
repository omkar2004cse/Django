from django import forms
from .models import chaiVarity

class chai_varity_from(forms.Form):
    chai_varity= forms.ModelChoiceField(queryset=chaiVarity.objects.all(),label="select chai variety")
