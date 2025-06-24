import json
from typing import Any
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CspReport


@csrf_exempt
def csp_report(request: HttpRequest) -> HttpResponse:
    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"}, status=405)

    try:
        payload: dict[str, Any] = json.loads(request.body.decode("utf-8"))
        report: dict[str, Any] = payload.get("csp-report", {})

        CspReport.objects.create(
            document_uri=report.get("document-uri", ""),
            referrer=report.get("referrer"),
            violated_directive=report.get("violated-directive", ""),
            effective_directive=report.get("effective-directive", ""),
            original_policy=report.get("original-policy", ""),
            disposition=report.get("disposition", ""),
            blocked_uri=report.get("blocked-uri"),
            line_number=report.get("line-number"),
            column_number=report.get("column-number"),
            source_file=report.get("source-file"),
            status_code=report.get("status-code"),
            script_sample=report.get("script-sample"),
        )
        return HttpResponse(status=204)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
