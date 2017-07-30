from django.shortcuts import render
from PersonInfoSite.models import Person
# Create your views here.

def person(request):
    persons = Person.objects.order_by('first_name')
    person_dic = {'persons':persons}
    return render(request,'PersonInfoSite/persons.html',context=person_dic)

def index(request):
    return render(request,'PersonInfoSite/HTML.html')
