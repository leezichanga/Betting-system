from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns=[
url('^$',views.home,name='home'),
url(r'^deposit/',views.deposit, name='deposit'),
url(r'^placebet/',views.place_bet, name='placebet'),
url(r'^ajax/view_balance/$', views.view_balance, name='balance'),
]
