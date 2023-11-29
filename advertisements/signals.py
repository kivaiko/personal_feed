from django.db.models.signals import post_save
from django.dispatch import receiver
from advertisements.models import Advertisement
from feed.models import AdvertisementEvent


@receiver(post_save, sender=Advertisement)
def create_advertisement_event(sender, instance, created, **kwargs):
    if created:
        AdvertisementEvent.objects.create(advertisement=instance)
