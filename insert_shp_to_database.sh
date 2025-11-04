#!/bin/zsh

cd Documents/TA/Learning/Django
source djgeovis/bin/activate
cd djgeovis/geovis/apps/maps/static/static_base/src
python3 shp_to_models.py -m $1 -v $2 -f $3
cd ../../../../../
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py shell << EOF
from apps.maps.static.static_base.src import mappings
mappings.run()
EOF
cd ../../../../../../
deactivate


