from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns=[
 url(r'^ajax/view_balance/$', views.view_balance, name='view_balance'),
]
