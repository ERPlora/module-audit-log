"""
Audit Trail Module Views
"""
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, render as django_render
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_POST

from apps.accounts.decorators import login_required, permission_required
from apps.core.htmx import htmx_view
from apps.core.services import export_to_csv, export_to_excel
from apps.modules_runtime.navigation import with_module_nav

from .models import AuditEntry

PER_PAGE_CHOICES = [10, 25, 50, 100]


# ======================================================================
# Dashboard
# ======================================================================

@login_required
@with_module_nav('audit_log', 'dashboard')
@htmx_view('audit_log/pages/index.html', 'audit_log/partials/dashboard_content.html')
def dashboard(request):
    hub_id = request.session.get('hub_id')
    return {
        'total_audit_entries': AuditEntry.objects.filter(hub_id=hub_id, is_deleted=False).count(),
    }


# ======================================================================
# AuditEntry
# ======================================================================

AUDIT_ENTRY_SORT_FIELDS = {
    'action': 'action',
    'entity_type': 'entity_type',
    'entity_id': 'entity_id',
    'user_id': 'user_id',
    'user_name': 'user_name',
    'ip_address': 'ip_address',
    'created_at': 'created_at',
}

def _build_audit_entries_context(hub_id, per_page=10):
    qs = AuditEntry.objects.filter(hub_id=hub_id, is_deleted=False).order_by('action')
    paginator = Paginator(qs, per_page)
    page_obj = paginator.get_page(1)
    return {
        'audit_entries': page_obj,
        'page_obj': page_obj,
        'search_query': '',
        'sort_field': 'action',
        'sort_dir': 'asc',
        'current_view': 'table',
        'per_page': per_page,
    }

def _render_audit_entries_list(request, hub_id, per_page=10):
    ctx = _build_audit_entries_context(hub_id, per_page)
    return django_render(request, 'audit_log/partials/audit_entries_list.html', ctx)

@login_required
@with_module_nav('audit_log', 'log')
@htmx_view('audit_log/pages/audit_entries.html', 'audit_log/partials/audit_entries_content.html')
def audit_entries_list(request):
    hub_id = request.session.get('hub_id')
    search_query = request.GET.get('q', '').strip()
    sort_field = request.GET.get('sort', 'action')
    sort_dir = request.GET.get('dir', 'asc')
    page_number = request.GET.get('page', 1)
    current_view = request.GET.get('view', 'table')
    per_page = int(request.GET.get('per_page', 10))
    if per_page not in PER_PAGE_CHOICES:
        per_page = 10

    qs = AuditEntry.objects.filter(hub_id=hub_id, is_deleted=False)

    if search_query:
        qs = qs.filter(Q(action__icontains=search_query) | Q(entity_type__icontains=search_query) | Q(user_name__icontains=search_query))

    order_by = AUDIT_ENTRY_SORT_FIELDS.get(sort_field, 'action')
    if sort_dir == 'desc':
        order_by = f'-{order_by}'
    qs = qs.order_by(order_by)

    export_format = request.GET.get('export')
    if export_format in ('csv', 'excel'):
        fields = ['action', 'entity_type', 'entity_id', 'user_id', 'user_name', 'ip_address']
        headers = ['Action', 'Entity Type', 'Entity Id', 'User Id', 'User Name', 'Ip Address']
        if export_format == 'csv':
            return export_to_csv(qs, fields=fields, headers=headers, filename='audit_entries.csv')
        return export_to_excel(qs, fields=fields, headers=headers, filename='audit_entries.xlsx')

    paginator = Paginator(qs, per_page)
    page_obj = paginator.get_page(page_number)

    if request.htmx and request.htmx.target == 'datatable-body':
        return django_render(request, 'audit_log/partials/audit_entries_list.html', {
            'audit_entries': page_obj, 'page_obj': page_obj,
            'search_query': search_query, 'sort_field': sort_field,
            'sort_dir': sort_dir, 'current_view': current_view, 'per_page': per_page,
        })

    return {
        'audit_entries': page_obj, 'page_obj': page_obj,
        'search_query': search_query, 'sort_field': sort_field,
        'sort_dir': sort_dir, 'current_view': current_view, 'per_page': per_page,
    }

@login_required
@htmx_view('audit_log/pages/audit_entry_add.html', 'audit_log/partials/audit_entry_add_content.html')
def audit_entry_add(request):
    hub_id = request.session.get('hub_id')
    if request.method == 'POST':
        action = request.POST.get('action', '').strip()
        entity_type = request.POST.get('entity_type', '').strip()
        entity_id = request.POST.get('entity_id', '').strip()
        user_id = request.POST.get('user_id', '').strip()
        user_name = request.POST.get('user_name', '').strip()
        ip_address = request.POST.get('ip_address', '').strip()
        details = request.POST.get('details', '').strip()
        obj = AuditEntry(hub_id=hub_id)
        obj.action = action
        obj.entity_type = entity_type
        obj.entity_id = entity_id
        obj.user_id = user_id
        obj.user_name = user_name
        obj.ip_address = ip_address
        obj.details = details
        obj.save()
        response = HttpResponse(status=204)
        response['HX-Redirect'] = reverse('audit_log:dashboard')
        return response
    return {}

@login_required
@htmx_view('audit_log/pages/audit_entry_edit.html', 'audit_log/partials/audit_entry_edit_content.html')
def audit_entry_edit(request, pk):
    hub_id = request.session.get('hub_id')
    obj = get_object_or_404(AuditEntry, pk=pk, hub_id=hub_id, is_deleted=False)
    if request.method == 'POST':
        obj.action = request.POST.get('action', '').strip()
        obj.entity_type = request.POST.get('entity_type', '').strip()
        obj.entity_id = request.POST.get('entity_id', '').strip()
        obj.user_id = request.POST.get('user_id', '').strip()
        obj.user_name = request.POST.get('user_name', '').strip()
        obj.ip_address = request.POST.get('ip_address', '').strip()
        obj.details = request.POST.get('details', '').strip()
        obj.save()
        return _render_audit_entries_list(request, hub_id)
    return {'obj': obj}

@login_required
@require_POST
def audit_entry_delete(request, pk):
    hub_id = request.session.get('hub_id')
    obj = get_object_or_404(AuditEntry, pk=pk, hub_id=hub_id, is_deleted=False)
    obj.is_deleted = True
    obj.deleted_at = timezone.now()
    obj.save(update_fields=['is_deleted', 'deleted_at', 'updated_at'])
    return _render_audit_entries_list(request, hub_id)

@login_required
@require_POST
def audit_entries_bulk_action(request):
    hub_id = request.session.get('hub_id')
    ids = [i.strip() for i in request.POST.get('ids', '').split(',') if i.strip()]
    action = request.POST.get('action', '')
    qs = AuditEntry.objects.filter(hub_id=hub_id, is_deleted=False, id__in=ids)
    if action == 'delete':
        qs.update(is_deleted=True, deleted_at=timezone.now())
    return _render_audit_entries_list(request, hub_id)


@login_required
@permission_required('audit_log.manage_settings')
@with_module_nav('audit_log', 'settings')
@htmx_view('audit_log/pages/settings.html', 'audit_log/partials/settings_content.html')
def settings_view(request):
    return {}

