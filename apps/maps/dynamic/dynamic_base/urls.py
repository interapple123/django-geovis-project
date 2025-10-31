from . import views
from django.urls import path

urlpatterns = [
    path("dynamic_base/", views.dynamic_base, name="dynamic_base"),
]
