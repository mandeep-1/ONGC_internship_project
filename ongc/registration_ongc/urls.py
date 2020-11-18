from django.contrib import admin
from django.urls import path
from registration_ongc import views
urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('officer', views.handelofficer, name='officer'),
    path('officerlogin', views.handleofficerLogin, name='handleofficerLogin'),
    path('officerlogout', views.handleofficerLogout, name='handleofficerLogout'),
    path('deleterecent', views.deleterecent, name='deleterecent'),
    path('acceptrecent', views.acceptrecent, name='acceptrecent'),
    path('sendmails', views.sendmails, name='sendmails'),
]
