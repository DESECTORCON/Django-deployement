from django.conf.urls import url
from eventhandler import views

app_name = 'eventhandler'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addevent/$', views.addevent, name='addevent'),
    url(r'^picrandomevent$', views.event, name='PicRandomEvent')
]
