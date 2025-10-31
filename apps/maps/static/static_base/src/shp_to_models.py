from django.contrib.gis.gdal import DataSource
from django.contrib.gis.gdal.field import (
    OFTDate,
    OFTDateTime,
    OFTInteger,
    OFTInteger64,
    OFTReal,
    OFTString,
    OFTTime,
)
from django.contrib.gis.utils import ogrinspect, mapping
import os
import argparse

parser = argparse.ArgumentParser(description="A script that processes user data.")

parser.add_argument('-m', '--model-name', type=str, help='Your model name')
parser.add_argument('-v', '--verbose-name', type=str, help='Your model verbose name')
parser.add_argument('-f', '--shp-file', type=str, help='Your shapefile path')

args = parser.parse_args()

model_name = None
model_verbose_name = None
shp_path = None

try:
    model_name = args.model_name
    model_verbose_name = args.verbose_name
    shp_path = args.shp_file
    print(f"Model Name: {model_name}")
    print(f"Model Verbose Name: {model_verbose_name}")
    print(f"Shapefile Path: {shp_path}")

    ds = DataSource(shp_path)

except TypeError :
     exit("Error: Please provide both model name, verbose name, and shp file path using -m, -v, and -f flags.")

append = f"""\n
    def __str__(self):
        return self.namobj

    class Meta:
        verbose_name = "{model_verbose_name}"
        verbose_name_plural = "{model_verbose_name}"
        ordering = ["objectid"]
"""

mapping_and_run = f"""import os
from django.contrib.gis.utils import LayerMapping
from ..models import {model_name}

{model_name}_shp = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), "{shp_path}"
    )
)

def run(verbose=True):
    lm = LayerMapping(
        {model_name},
        {model_name}_shp,
        {model_name}_mapping,
        transform=False,
        encoding="iso-8859-1",
    )
    lm.save(strict=True, verbose=verbose)
"""

def run():
    output = ogrinspect(shp_path, model_name, multi_geom=True, srid=4326,
                        geom_name='geom', blank=True, null=True)
    mapping_dict = mapping(ds)
    mapping_dict_script = f"\n{model_name}_mapping = " + str(mapping_dict)
    mapping_and_run_script = mapping_and_run + mapping_dict_script
    with open("../models/gis_models.py", "a") as f:
        f.write( "\n" + output + append)
    with open("mappings.py", "w") as f:
        f.write(mapping_and_run_script)
    with open("../models/__init__.py", "a") as f:
        f.write(f'\n__all__.append("{model_name}")')
    with open("../admin.py", "a") as f:
        f.write(f'\nadmin.site.register({model_name})')

if __name__ == "__main__":
    run()