from .tle import insert_tle, get_tle_by_name
from skyfield.api import load, EarthSatellite
from sgp4 import exporter
from datetime import timedelta
from typing import Optional, Iterable, Dict, Tuple, Any

def propagate_tles() -> None:
    """
    Calls CelesTrak API and pushes recent TLE data to database
    """

    url = 'http://celestrak.com/NORAD/elements/stations.txt'

    satellites = load.tle_file(url)

    print("total satellites: ", len(satellites))

    for satellite in satellites:
        print(satellite.name, satellite.model)
        raw_tle = exporter.export_tle(satellite.model)
        print(raw_tle)
        line_1 = raw_tle[0]
        line_2 = raw_tle[1]
        tle_dict = {
            "sat_id": satellite.model.satnum,
            "sat_name": satellite.name,
            "line_1": line_1,
            "line_2": line_2,
            "source": 'CelesTrak'
        }

        insert_tle(tle_dict)
        print(convert_tle_to_coords(satellite.name))

    print("Insertion Complete")

def convert_tle_to_coords(sat_name: str) -> dict[str, Any]:
    """
    Converts satellite entity into a Three-point cartesian coordinate for the frontend

    Parameters:
    - sat_name: name of satellite to convert

    Returns: dictionary representation of cartesian coordinate
    """

    # setup satellite
    ts = load.timescale()
    sat_dict = get_tle_by_name(sat_name)
    satellite = EarthSatellite(sat_dict['line1'], sat_dict['line2'], sat_dict['name'], ts)

    # get geocentric location of satellite
    x, y, z = list(map(float, satellite.at(ts.now()).xyz.km))

    # sanitize to threejs coordinates (in meters)
    return {
        "x": x / 1000,
        "y": y / 1000,
        "z": z / 1000,
    }
