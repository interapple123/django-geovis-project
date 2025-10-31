from django.apps import AppConfig


class StaticBaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.maps.static.static_base'
