"""
AI context for the Audit Log module.
Loaded into the assistant system prompt when this module's tools are active.
"""

CONTEXT = """
## Module Knowledge: Audit Log

### Models

**AuditEntry** — immutable record of an action performed in the system.
- `action` (str, max 30): the operation performed (e.g. "create", "update", "delete", "login")
- `entity_type` (str, max 100): the model/resource affected (e.g. "inventory.Product", "sales.Sale")
- `entity_id` (UUID, nullable): PK of the affected object
- `user_id` (UUID, nullable): PK of the user who performed the action
- `user_name` (str): display name of the user at time of action
- `ip_address` (nullable): IP of the request
- `details` (JSON dict): extra context — changed fields, old/new values, etc.
- `timestamp` (datetime, auto): when the action occurred

### Key flows

1. **Logging an action**: create an AuditEntry with action, entity_type, entity_id, user_id, user_name, and a details dict describing what changed.
2. **Querying the log**: filter by entity_type + entity_id to see full history of one record; filter by user_id to see all actions by a user; filter by action to find all deletes/creates.
3. **Audit entries are append-only** — they should never be updated or deleted.

### Notes
- `details` JSON typically contains: `{"before": {...}, "after": {...}}` or `{"fields_changed": [...]}`.
- `entity_type` follows the pattern `"app_label.ModelName"` (e.g. `"customers.Customer"`).
- No FK relations to other tables — all references stored as UUIDs and name copies to preserve history even if source records are deleted.
"""
