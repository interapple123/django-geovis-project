from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("static_map", views.static_map, name="static_map"),
    path("dynamic_map", views.dynamic_map, name="dynamic_map"),
]
