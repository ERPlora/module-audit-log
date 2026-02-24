from django.urls import path
from . import views

app_name = 'audit_log'

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # AuditEntry
    path('audit_entries/', views.audit_entries_list, name='audit_entries_list'),
    path('audit_entries/add/', views.audit_entry_add, name='audit_entry_add'),
    path('audit_entries/<uuid:pk>/edit/', views.audit_entry_edit, name='audit_entry_edit'),
    path('audit_entries/<uuid:pk>/delete/', views.audit_entry_delete, name='audit_entry_delete'),
    path('audit_entries/bulk/', views.audit_entries_bulk_action, name='audit_entries_bulk_action'),

    # Settings
    path('settings/', views.settings_view, name='settings'),
]
