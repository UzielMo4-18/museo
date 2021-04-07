from django import forms
from .models import Visita

class VisitaEntryForm(forms.ModelForm):
    class Meta:
        model=Visita
        fields='__all__'
        exclude=['timestamp_out','comment']

class VisitaExitForm(forms.ModelForm):
    class Meta:
        model=Visita
        fields='__all__'
        exclude=['email','timestamp_in']