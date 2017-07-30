from django.conf.urls import url
from PersonInfoSite import views

urlpatterns = [
    url(r'^$', views.person, name='persons')
]
