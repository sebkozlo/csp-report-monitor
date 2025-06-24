from django.urls import path
from . import views

urlpatterns = [
    path("csp-report/", views.csp_report, name="csp_report"),
]
