"""Tests for audit_log models."""
import pytest
from django.utils import timezone

from audit_log.models import AuditEntry


@pytest.mark.django_db
class TestAuditEntry:
    """AuditEntry model tests."""

    def test_create(self, audit_entry):
        """Test AuditEntry creation."""
        assert audit_entry.pk is not None
        assert audit_entry.is_deleted is False

    def test_soft_delete(self, audit_entry):
        """Test soft delete."""
        pk = audit_entry.pk
        audit_entry.is_deleted = True
        audit_entry.deleted_at = timezone.now()
        audit_entry.save()
        assert not AuditEntry.objects.filter(pk=pk).exists()
        assert AuditEntry.all_objects.filter(pk=pk).exists()

    def test_queryset_excludes_deleted(self, hub_id, audit_entry):
        """Test default queryset excludes deleted."""
        audit_entry.is_deleted = True
        audit_entry.deleted_at = timezone.now()
        audit_entry.save()
        assert AuditEntry.objects.filter(hub_id=hub_id).count() == 0


