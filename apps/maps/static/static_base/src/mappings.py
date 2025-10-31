import os
from django.contrib.gis.utils import LayerMapping
from ..models import Migas

Migas_shp = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), "/home/fhs/shptest/03_MIGAS_TANPA_Z.shp"
    )
)

def run(verbose=True):
    lm = LayerMapping(
        Migas,
        Migas_shp,
        Migas_mapping,
        transform=False,
        encoding="iso-8859-1",
    )
    lm.save(strict=True, verbose=verbose)

Migas_mapping = {'objectid': 'OBJECTID', 'namobj': 'NAMOBJ', 'orde01': 'ORDE01', 'orde02': 'ORDE02', 'orde03': 'ORDE03', 'orde04': 'ORDE04', 'jnsrsr': 'JNSRSR', 'stsjrn': 'STSJRN', 'wadmpr': 'WADMPR', 'remark': 'REMARK', 'sbdata': 'SBDATA', 'shape_leng': 'SHAPE_Leng', 'geom': 'LINESTRING'}