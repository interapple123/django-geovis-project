from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse
from django.core.serializers import serialize
from django.conf import settings
from .models import *
from .utils import move_files_from_base_to_app, process_shp_zip_file
import os
import json

# Create your views here.

longitude = None
latitude = None

def alurpelayaran_datasets(request):
    alurpelayaran = serialize("geojson", AlurPelayaran.objects.all())
    return HttpResponse(alurpelayaran, content_type="json")

def upload_file(request):
    source = os.path.join(settings.BASE_DIR, "media", "data")
    destination = os.path.join(
        settings.BASE_DIR, "apps", "maps", "static", "static_base", "media", "data", "upload"
    )
    if request.method == "POST":
        form = ZipFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            move_files_from_base_to_app(
                source,
                destination,
            )
            zipfilename = request.FILES['zipfile'].name
            geojson_path = process_shp_zip_file(zipfilename, destination)
            return HttpResponse(status=204)
        else:
            return HttpResponse(status=400)
    else:
        form = ZipFileForm()
        return HttpResponse(status=405)

def serve_geojson(request):
    geojson_path = os.path.join(
        settings.BASE_DIR,
        "apps",
        "maps",
        "static",
        "static_base",
        "media",
        "data",
        "upload",
        f"uploaded.geojson",
    )
    return FileResponse(open(geojson_path, 'rb'), content_type='application/json')

def input_marker_coords(request):
    global latitude, longitude
    if request.method == "POST":
        form = CoordsForm(request.POST)
        if form.is_valid():
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']
            coords = (latitude, longitude)
            return render(request, 'static/input_coords_form.html')
        else:
            return render(request, 'static/input_coords_form.html', {'form': form})
    return render(request, 'static/input_coords_form.html')

def receive_marker_coords(request):
    global latitude, longitude
    if latitude is not None and longitude is not None:
        data = {
            'latitude': latitude,
            'longitude': longitude
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'No coordinates available'}, status=400)
