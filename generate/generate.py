from collections import OrderedDict
import fiona
import json
from numpy.random import default_rng


rng = default_rng()

n = 1000
lons = rng.uniform(-180, 180, n)
lats = rng.uniform(-90, 90, n)
pairs = zip(lons, lats)


def create_feature(lon, lat):
    return {
        "type": "Feature",
        "properties": OrderedDict(),
        "geometry": {"type": "Point", "coordinates": (lon, lat)},
    }


features = [create_feature(pair[0], pair[1]) for pair in pairs]

geodata = {
    "type": "FeatureCollection",
    "features": features,
}

with open("./output.geojson", "w") as f:
    f.write(json.dumps(geodata))
