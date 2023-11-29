from django.db.models.signals import post_save
from django.dispatch import receiver
from feed.models import NoteEvent
from notes.models import Note


@receiver(post_save, sender=Note)
def create_note_event(sender, instance, created, **kwargs):
    if created:
        NoteEvent.objects.create(note=instance)
