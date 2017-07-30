from django.shortcuts import render
from eventhandler.models import Event
from . import forms
from django.contrib.auth.decorators import login_required


@login_required
def event(request):
    event = Event.objects.order_by('event_text')
    event_dic = {'event':event}
    return render(request,'eventhandler/PicRandomEvent.html',context=event_dic)

def index(request):
    return render(request, 'eventhandler/MainEventSite.html',{})

@login_required
def addevent(request):
    form = forms.NewEvent()

    if request.method == 'POST':
        form = forms.NewEvent(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return event(request)

        else:
            print('ERROR FORM INVALID')

    return render(request,'eventhandler/AddEvent.html',{'form':form})
