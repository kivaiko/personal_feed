from django.contrib import admin
from polymorphic.admin import (
    PolymorphicParentModelAdmin,
    PolymorphicChildModelAdmin,
)
from .models import FeedEvent, AdvertisementEvent, AchievementEvent, NoteEvent


class AdvertisementEventAdmin(PolymorphicChildModelAdmin):
    base_model = AdvertisementEvent


class AchievementEventAdmin(PolymorphicChildModelAdmin):
    base_model = AchievementEvent


class NoteEventAdmin(PolymorphicChildModelAdmin):
    base_model = NoteEvent


class FeedEventAdmin(PolymorphicParentModelAdmin):
    base_model = FeedEvent
    child_models = (AdvertisementEvent, AchievementEvent, NoteEvent)
    list_display = ["created_at"]


admin.site.register(FeedEvent, FeedEventAdmin)
admin.site.register(AdvertisementEvent, AdvertisementEventAdmin)
admin.site.register(AchievementEvent, AchievementEventAdmin)
admin.site.register(NoteEvent, NoteEventAdmin)
