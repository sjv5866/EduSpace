from .db_utils import exec_commit
from skyfield.api import load, EarthSatellite
from sgp4 import exporter

def propagate_tles() -> None:

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

        insert_sql = """
            INSERT INTO tles(satellite_id, satellite_name, line1, line2, source)
            VALUES (%(sat_id)s, %(sat_name)s, %(line_1)s, %(line_2)s, %(source)s)
            ON CONFLICT(satellite_id)
            DO UPDATE SET 
                inserted_at = NOW();
        """
        exec_commit(insert_sql, tle_dict)

    print("Insertion Complete")