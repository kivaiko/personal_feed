from django.db.models.signals import post_save
from django.dispatch import receiver
from achievements.models import UserAchievement
from feed.models import AchievementEvent
import logging


logger = logging.getLogger(__name__)


@receiver(post_save, sender=UserAchievement)
def create_achievement_event(sender, instance, created, **kwargs):
    if created:
        try:
            achievement_event = AchievementEvent.objects.create(
                achievement=instance
            )
            logger.debug(f"AchievementEvent created: {achievement_event.id}")
        except Exception as e:
            logger.error(f"Error creating AchievementEvent: {e}")
