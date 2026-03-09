# Audit Trail

## Overview

| Property | Value |
|----------|-------|
| **Module ID** | `audit_log` |
| **Version** | `1.0.0` |
| **Icon** | `eye-outline` |
| **Dependencies** | None |

## Models

### `AuditEntry`

AuditEntry(id, hub_id, created_at, updated_at, created_by, updated_by, is_deleted, deleted_at, action, entity_type, entity_id, user_id, user_name, ip_address, details, timestamp)

| Field | Type | Details |
|-------|------|---------|
| `action` | CharField | max_length=30 |
| `entity_type` | CharField | max_length=100 |
| `entity_id` | UUIDField | max_length=32, optional |
| `user_id` | UUIDField | max_length=32, optional |
| `user_name` | CharField | max_length=255, optional |
| `ip_address` | GenericIPAddressField | max_length=39, optional |
| `details` | JSONField | optional |
| `timestamp` | DateTimeField | optional |

## URL Endpoints

Base path: `/m/audit_log/`

| Path | Name | Method |
|------|------|--------|
| `(root)` | `dashboard` | GET |
| `log/` | `log` | GET |
| `audit_entries/` | `audit_entries_list` | GET |
| `audit_entries/add/` | `audit_entry_add` | GET/POST |
| `audit_entries/<uuid:pk>/edit/` | `audit_entry_edit` | GET |
| `audit_entries/<uuid:pk>/delete/` | `audit_entry_delete` | GET/POST |
| `audit_entries/bulk/` | `audit_entries_bulk_action` | GET/POST |
| `settings/` | `settings` | GET |

## Permissions

| Permission | Description |
|------------|-------------|
| `audit_log.view_auditentry` | View Auditentry |
| `audit_log.manage_settings` | Manage Settings |

**Role assignments:**

- **admin**: All permissions
- **manager**: `view_auditentry`
- **employee**: `view_auditentry`

## Navigation

| View | Icon | ID | Fullpage |
|------|------|----|----------|
| Dashboard | `speedometer-outline` | `dashboard` | No |
| Log | `eye-outline` | `log` | No |
| Settings | `settings-outline` | `settings` | No |

## AI Tools

Tools available for the AI assistant:

### `list_audit_entries`

List audit log entries (read-only). Shows who did what and when.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `action` | string | No |  |
| `entity_type` | string | No |  |
| `user_id` | string | No |  |
| `date_from` | string | No |  |
| `date_to` | string | No |  |
| `limit` | integer | No |  |

## File Structure

```
README.md
__init__.py
admin.py
ai_tools.py
apps.py
forms.py
locale/
  en/
    LC_MESSAGES/
      django.po
  es/
    LC_MESSAGES/
      django.po
migrations/
  0001_initial.py
  __init__.py
models.py
module.py
static/
  audit_log/
    css/
    js/
  icons/
    icon.svg
templates/
  audit_log/
    pages/
      audit_entries.html
      audit_entry_add.html
      audit_entry_edit.html
      dashboard.html
      index.html
      log.html
      settings.html
    partials/
      audit_entries_content.html
      audit_entries_list.html
      audit_entry_add_content.html
      audit_entry_edit_content.html
      dashboard_content.html
      log_content.html
      panel_audit_entry_add.html
      panel_audit_entry_edit.html
      settings_content.html
tests/
  __init__.py
  conftest.py
  test_models.py
  test_views.py
urls.py
views.py
```
