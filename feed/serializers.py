from rest_framework import serializers
from achievements.models import UserAchievement
from advertisements.models import Advertisement
from notes.models import Note
from .models import FeedEvent, AdvertisementEvent, AchievementEvent, NoteEvent


class FeedNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "body"]


class FeedAchievementSerializer(serializers.ModelSerializer):
    achievement = serializers.CharField(source="achievement.name")
    description = serializers.CharField(source="achievement.description")
    icon = serializers.ImageField(source="achievement.icon", use_url=True)

    class Meta:
        model = UserAchievement
        fields = ["id", "achievement", "description", "icon"]


class FeedAdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ["id", "title", "description", "image", "link"]

    image = serializers.ImageField(use_url=True)


class FeedEventSerializer(serializers.ModelSerializer):
    detail = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()

    class Meta:
        model = FeedEvent
        fields = ["id", "type", "created_at", "detail"]

    def get_detail(self, obj):
        if isinstance(obj, NoteEvent):
            return FeedNoteSerializer(obj.note).data
        elif isinstance(obj, AchievementEvent):
            return FeedAchievementSerializer(obj.achievement).data
        elif isinstance(obj, AdvertisementEvent):
            return FeedAdvertisementSerializer(obj.advertisement).data
        return None

    def get_type(self, obj):
        if isinstance(obj, NoteEvent):
            return "note"
        elif isinstance(obj, AchievementEvent):
            return "achievement"
        elif isinstance(obj, AdvertisementEvent):
            return "advertisement"
        return "unknown"
