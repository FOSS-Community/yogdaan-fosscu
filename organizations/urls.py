from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('2023/organizations', views.organizations, name= 'organizations-info')
]