"""
Audit Trail Module Views
"""
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from apps.accounts.decorators import login_required
from apps.core.htmx import htmx_view
from apps.modules_runtime.navigation import with_module_nav


@login_required
@with_module_nav('audit_log', 'dashboard')
@htmx_view('audit_log/pages/dashboard.html', 'audit_log/partials/dashboard_content.html')
def dashboard(request):
    """Dashboard view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('audit_log', 'log')
@htmx_view('audit_log/pages/log.html', 'audit_log/partials/log_content.html')
def log(request):
    """Log view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('audit_log', 'settings')
@htmx_view('audit_log/pages/settings.html', 'audit_log/partials/settings_content.html')
def settings(request):
    """Settings view."""
    hub_id = request.session.get('hub_id')
    return {}

