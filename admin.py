from django.contrib import admin

from .models import AuditEntry

@admin.register(AuditEntry)
class AuditEntryAdmin(admin.ModelAdmin):
    list_display = ['action', 'entity_type', 'entity_id', 'user_id', 'user_name', 'created_at']
    search_fields = ['action', 'entity_type', 'user_name']
    readonly_fields = ['created_at', 'updated_at']

