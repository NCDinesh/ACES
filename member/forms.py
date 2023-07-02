from django import forms
from .models import member

class memberform(forms.ModelForm):
    class Meta:
        model=member
        fields=['name','email','message']