from django.shortcuts import render
# from django.http import HttpResponse
# from AppTwo.models import First_Name,Last_Name,Email
from AppTwo.forms import NewUserForm
from AppTwo.models import User
# Create your views here.

def index(request):

    userss = User.objects.order_by('first_name')
    dic = {'users':userss}

    return render(request,'AppTwo/index.html',context=dic)

def users(request):

    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print('ERROR FORM INVALID')

    return render(request,'AppTwo/user.html',{'form':form})
