from django.shortcuts import render
from PersonInfoSite.models import Person
from . import forms
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def person(request):
    persons = Person.objects.order_by('first_name')
    person_dic = {'persons':persons}
    return render(request,'PersonInfoSite/persons.html',context=person_dic)

def index(request):
    return render(request,'PersonInfoSite/HTML.html')

@login_required
def addperson(request):
    form = forms.NewPerson()

    if request.method == 'POST':
        form = forms.NewPerson(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return person(request)

        else:
            print('ERROR FORM INVALID')

    return render(request,'PersonInfoSite/AddPerson.html',{'form':form})
