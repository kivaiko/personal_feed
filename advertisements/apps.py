from django.apps import AppConfig


class AdvertisementsConfig(AppConfig):
    name = "advertisements"

    def ready(self):
        import advertisements.signals
