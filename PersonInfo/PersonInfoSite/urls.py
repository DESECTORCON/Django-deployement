from django.conf.urls import url
from PersonInfoSite import views

app_name = 'PersonInfo'

urlpatterns = [
    url(r'^$', views.person, name='persons'),
    url(r'^/addperson/',views.addperson,name='addperson')
]
