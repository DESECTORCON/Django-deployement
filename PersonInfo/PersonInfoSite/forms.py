from django import forms
from PersonInfoSite.models import Person

class NewPerson(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()
    height = forms.IntegerField(max_value=200)
    age = forms.IntegerField(max_value=100)

    class Meta:
        model = Person
        fields = '__all__'
