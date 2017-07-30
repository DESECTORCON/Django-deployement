from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import First_Name,Last_Name,Email

# Create your views here.
def user(request):
    User_First_Name = First_Name.objects.order_by('First_Name')
    User_Last_Name = Last_Name.objects.order_by('Last_Name')
    User_Email = Email.objects.order_by('Email')
    dic = {'First_Name':User_First_Name,'Last_Name':User_Last_Name,'Email':User_Email}
    return render(request,'AppTwo/Help.html', context=dic)
