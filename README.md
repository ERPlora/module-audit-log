# Audit Trail Module

Comprehensive audit trail for all system actions.

## Features

- Automatic logging of system actions (create, update, delete, etc.)
- Track which user performed each action with user ID and name
- Entity type and ID tracking for affected records
- IP address recording for each action
- JSON details field for storing additional action context
- Automatic timestamp on every entry

## Installation

This module is installed automatically via the ERPlora Marketplace.

## Configuration

Access settings via: **Menu > Audit Trail > Settings**

## Usage

Access via: **Menu > Audit Trail**

### Views

| View | URL | Description |
|------|-----|-------------|
| Dashboard | `/m/audit_log/dashboard/` | Overview of recent audit activity |
| Log | `/m/audit_log/log/` | Full audit log with filtering and search |
| Settings | `/m/audit_log/settings/` | Module configuration |

## Models

| Model | Description |
|-------|-------------|
| `AuditEntry` | Audit log entry with action, entity type/ID, user info, IP address, details, and timestamp |

## Permissions

| Permission | Description |
|------------|-------------|
| `audit_log.view_auditentry` | View audit log entries |
| `audit_log.manage_settings` | Manage module settings |

## License

MIT

## Author

ERPlora Team - support@erplora.com
