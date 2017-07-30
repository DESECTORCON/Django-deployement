from django import forms
from eventhandler.models import Event

class NewEvent(forms.ModelForm):
    event_text = forms.TextInput()

    class Meta:
        model = Event
        fields = '__all__'
