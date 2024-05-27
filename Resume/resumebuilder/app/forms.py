from django import forms 
from .models import *


class ResumeForm(forms.ModelForm):
    class Meta:
        model=Resume
        fields='__all__'


class SendemailForm(forms.ModelForm):
    class Meta:
        model=SendEmail
        fields='__all__'




