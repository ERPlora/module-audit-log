from django.urls import path
from . import views

app_name = 'audit_log'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('log/', views.log, name='log'),
    path('settings/', views.settings, name='settings'),
]
