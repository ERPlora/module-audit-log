from django import forms
from django.utils.translation import gettext_lazy as _

from .models import AuditEntry

class AuditEntryForm(forms.ModelForm):
    class Meta:
        model = AuditEntry
        fields = ['action', 'entity_type', 'entity_id', 'user_id', 'user_name', 'ip_address', 'details']
        widgets = {
            'action': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'entity_type': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'entity_id': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'user_id': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'user_name': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'ip_address': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'details': forms.Textarea(attrs={'class': 'textarea textarea-sm w-full', 'rows': 3}),
        }

