from django.apps import AppConfig


class AchievementsConfig(AppConfig):
    name = "achievements"

    def ready(self):
        import achievements.signals
