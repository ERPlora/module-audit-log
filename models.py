from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models.base import HubBaseModel

class AuditEntry(HubBaseModel):
    action = models.CharField(max_length=30, verbose_name=_('Action'))
    entity_type = models.CharField(max_length=100, verbose_name=_('Entity Type'))
    entity_id = models.UUIDField(null=True, blank=True, verbose_name=_('Entity Id'))
    user_id = models.UUIDField(null=True, blank=True, verbose_name=_('User Id'))
    user_name = models.CharField(max_length=255, blank=True, verbose_name=_('User Name'))
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name=_('Ip Address'))
    details = models.JSONField(default=dict, blank=True, verbose_name=_('Details'))
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name=_('Timestamp'))

    class Meta(HubBaseModel.Meta):
        db_table = 'audit_log_auditentry'

    def __str__(self):
        return str(self.id)

