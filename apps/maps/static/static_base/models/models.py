from django.db import models
from django.forms import ModelForm

class ZipFile(models.Model):
    zipfile = models.FileField(upload_to='data/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.zipfile.name

class ZipFileForm(ModelForm):
    class Meta:
        model = ZipFile
        fields = ['zipfile']
        labels = {
            'zipfile': 'Select a zip file to upload',
        }
        help_texts = {
            'zipfile': 'Max. 42 megabytes',
        }

class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Coords({self.latitude}, {self.longitude})"

class CoordsForm(ModelForm):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude']
        labels = {
            'latitude': 'Latitude',
            'longitude': 'Longitude',
        }
        help_texts = {
            'latitude': 'Enter the latitude value',
            'longitude': 'Enter the longitude value',
        }