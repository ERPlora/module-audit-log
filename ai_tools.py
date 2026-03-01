"""AI tools for the Audit Log module."""
from assistant.tools import AssistantTool, register_tool


@register_tool
class ListAuditEntries(AssistantTool):
    name = "list_audit_entries"
    description = "List audit log entries (read-only). Shows who did what and when."
    module_id = "audit_log"
    required_permission = "audit_log.view_auditentry"
    parameters = {
        "type": "object",
        "properties": {
            "action": {"type": "string"}, "entity_type": {"type": "string"},
            "user_id": {"type": "string"}, "date_from": {"type": "string"},
            "date_to": {"type": "string"}, "limit": {"type": "integer"},
        },
        "required": [],
        "additionalProperties": False,
    }

    def execute(self, args, request):
        from audit_log.models import AuditEntry
        qs = AuditEntry.objects.all()
        if args.get('action'):
            qs = qs.filter(action__icontains=args['action'])
        if args.get('entity_type'):
            qs = qs.filter(entity_type=args['entity_type'])
        if args.get('user_id'):
            qs = qs.filter(user_id=args['user_id'])
        if args.get('date_from'):
            qs = qs.filter(timestamp__date__gte=args['date_from'])
        if args.get('date_to'):
            qs = qs.filter(timestamp__date__lte=args['date_to'])
        limit = args.get('limit', 20)
        return {"entries": [{"id": str(e.id), "action": e.action, "entity_type": e.entity_type, "user_name": e.user_name, "timestamp": e.timestamp.isoformat(), "ip_address": e.ip_address} for e in qs.order_by('-timestamp')[:limit]]}
