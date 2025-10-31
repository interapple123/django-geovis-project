from django.apps import AppConfig


class DynamicBaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.maps.dynamic.dynamic_base'
