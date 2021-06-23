from django.apps import AppConfig


class OliverConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'oliver'

    def ready(self):
        import oliver.signals

