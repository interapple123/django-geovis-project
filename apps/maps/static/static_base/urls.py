from . import views
from django.urls import path

urlpatterns = [
    path("alurpelayaran_data/", views.alurpelayaran_datasets, name="alurpelayaran"),
    path("api/input/", views.input_marker_coords, name="input_marker_coords"),
    path("api/input/markercoords/", views.receive_marker_coords, name="receive_marker_coords"),
    path("api/upload/", views.upload_file, name="upload_file"),
    path('api/upload/geojson/', views.serve_geojson, name='serve_geojson'),
]
