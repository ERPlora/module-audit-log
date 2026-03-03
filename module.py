from django.utils.translation import gettext_lazy as _

MODULE_ID = 'audit_log'
MODULE_NAME = _('Audit Trail')
MODULE_VERSION = '1.0.0'
MODULE_ICON = 'eye-outline'
MODULE_DESCRIPTION = _('Comprehensive audit trail for all system actions')
MODULE_AUTHOR = 'ERPlora'
MODULE_CATEGORY = 'compliance'

MENU = {
    'label': _('Audit Trail'),
    'icon': 'eye-outline',
    'order': 83,
}

NAVIGATION = [
    {'label': _('Dashboard'), 'icon': 'speedometer-outline', 'id': 'dashboard'},
{'label': _('Log'), 'icon': 'eye-outline', 'id': 'log'},
{'label': _('Settings'), 'icon': 'settings-outline', 'id': 'settings'},
]

DEPENDENCIES = []

PERMISSIONS = [
    'audit_log.view_auditentry',
'audit_log.manage_settings',
]

ROLE_PERMISSIONS = {
    "admin": ["*"],
    "manager": [
        "view_auditentry",
    ],
    "employee": [
        "view_auditentry",
    ],
}
