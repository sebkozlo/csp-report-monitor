from django.db import models


class CspReport(models.Model):
    document_uri = models.URLField()
    referrer = models.TextField(blank=True, null=True)
    violated_directive = models.CharField(max_length=255)
    effective_directive = models.CharField(max_length=255)
    original_policy = models.TextField()
    disposition = models.CharField(max_length=50)
    blocked_uri = models.TextField(blank=True, null=True)
    line_number = models.IntegerField(blank=True, null=True)
    column_number = models.IntegerField(blank=True, null=True)
    source_file = models.TextField(blank=True, null=True)
    status_code = models.IntegerField(blank=True, null=True)
    script_sample = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"CSP Violation at {self.document_uri}"
