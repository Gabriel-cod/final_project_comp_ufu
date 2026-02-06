from django.contrib import admin
from .models import Status, OperatorFleet, OperatorProfessional

@admin.register(Status)
class StatusRegister(admin.ModelAdmin):
    list_display = ("id", "status_name")
    search_fields = ("id", "status_name")

@admin.register(OperatorProfessional)
class OperatorProfessionalRegister(admin.ModelAdmin):
    list_display = ("id", "name", "role", "status")
    search_fields = ("id", "name", "role", "status")

@admin.register(OperatorFleet)
class OperatorFleetRegister(admin.ModelAdmin):
    list_display = ("id", "fleet_type", "fleet_model", "status")
    search_fields = ("id", "fleet_type", "fleet_model", "status")
