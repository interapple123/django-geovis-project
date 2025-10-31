import os
import zipfile as zip
import geopandas as gpd
from django.conf import settings

def move_files_from_base_to_app(source, destination):
    pathToProject = settings.BASE_DIR
    source = os.path.join(pathToProject, source)
    destination = os.path.join(pathToProject, destination)
    if not os.path.exists(destination):
        os.makedirs(destination)
    for filename in os.listdir(source):
        src_file = os.path.join(source, filename)
        dest_file = os.path.join(destination, filename)
        if os.path.isfile(src_file):
            os.rename(src_file, dest_file)

def process_shp_zip_file(filename, outputdir):
    filepath = os.path.join(outputdir, filename)
    with zip.ZipFile(filepath, "r") as zip_ref:
        zip_ref.extractall(os.path.dirname(filepath))

    shp_file = os.path.join(outputdir, filename.replace('.zip', '.shp'))
    
    gdf = gpd.read_file(os.path.join(os.path.dirname(filepath), shp_file))
    gdf = gdf.to_crs(epsg=4326)
    output_geojson_path = os.path.join(outputdir, f'uploaded.geojson')
    gdf.to_file(output_geojson_path, driver='GeoJSON', encoding='utf-8')
    return output_geojson_path
    
    