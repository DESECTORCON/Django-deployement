from django.conf.urls import url
from AppTwo import views

urlpatterns=[
    url('^$', views.user, name='user')
]
