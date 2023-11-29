from django.contrib import admin
from .models import Advertisement


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "link")
    search_fields = ("title", "description")
    list_filter = ("created_at",)
