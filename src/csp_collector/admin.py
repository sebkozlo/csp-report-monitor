from django.contrib import admin
from django.http import HttpRequest
from typing import Optional
from .models import CspReport


@admin.register(CspReport)
class CspReportAdmin(admin.ModelAdmin):
    list_display: tuple[str, ...] = (
        "created_at",
        "violated_directive",
        "blocked_uri",
        "document_uri",
        "source_file",
        "line_number",
    )
    list_filter: tuple[str, ...] = (
        "violated_directive",
        "disposition",
        "created_at",
    )
    search_fields: tuple[str, ...] = (
        "document_uri",
        "blocked_uri",
        "source_file",
        "violated_directive",
        "original_policy",
    )
    readonly_fields: list[str] = [f.name for f in CspReport._meta.fields]
    ordering: list[str] = ["-created_at"]

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

    def has_change_permission(
        self, request: HttpRequest, obj: Optional[CspReport] = None
    ) -> bool:
        return False

    def has_delete_permission(
        self, request: HttpRequest, obj: Optional[CspReport] = None
    ) -> bool:
        return True
