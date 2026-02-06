from django.contrib import admin
from .models import Mission

@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "mission_date",
        "description",
        "status"
    )
    list_filter = (
        "id",
        "mission_date",
        "description",
        "status"
    )
