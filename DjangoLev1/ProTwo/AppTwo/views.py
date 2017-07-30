from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def help(request):
    dic = {'msg':'Help Page'}
    return render(request,'AppTwo/Help.html', context=dic)