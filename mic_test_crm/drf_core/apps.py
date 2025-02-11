from django.apps import AppConfig


class DrfCoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'drf_core'

    def ready(self):
        import drf_core.signals  # Đăng ký signal