from django.forms import ModelForm
from gate_entry_app.models import Person, AttendanceHistory, Role, Gate, Device
from django import forms


class EntryExitSimulationForm(forms.Form):
    person = forms.ChoiceField(widget=forms.Select, choices=())
    device = forms.ChoiceField(widget=forms.Select, choices=())
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M:%S'],
                               widget=forms.DateTimeInput(format='%d/%m/%Y %H:%M:%S', attrs={'type': 'datetime-local'}))
