from polymorphic.models import PolymorphicModel
from django.db import models
from achievements.models import UserAchievement
from advertisements.models import Advertisement
from notes.models import Note


class FeedEvent(PolymorphicModel):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]


class AdvertisementEvent(FeedEvent):
    advertisement = models.ForeignKey(
        Advertisement,
        related_name="advertisement_events",
        on_delete=models.CASCADE,
    )


class AchievementEvent(FeedEvent):
    achievement = models.ForeignKey(
        UserAchievement,
        related_name="achievement_events",
        on_delete=models.CASCADE,
    )


class NoteEvent(FeedEvent):
    note = models.ForeignKey(
        Note, related_name="note_events", on_delete=models.CASCADE
    )
