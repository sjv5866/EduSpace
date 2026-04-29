from .db_utils import exec_get_all, exec_commit, exec_get_one
from typing import Optional, Iterable, Tuple, Any

def tuple_to_tle_dict(tle: Tuple[int, int, str, str, str, Any]) -> dict[str, Any]:
  """
  Helper function to convert TLE tuple into Flask-friendly format

  Parameters:
  - tle: Tuple representation of TLE data: [id, satellite id, satellite name, TLE line 1, TLE line 2, TLE source, and date inserted into database]

  Returns: dictionary representation of TLE tuple
  """
  
  id, satelliteId, name, line1, line2, source, inserted = tle
  return {
    "id": id,
    "satelliteId": satelliteId,
    "name": name,
    "line1": line1,
    "line2": line2,
    "source": source,
    "inserted": str(inserted),
  }

def insert_tle(sat_info: dict[str, Any]) -> None:
  """
  Pushes TLE to database. If existing satellite is found, replace tle lines and date of insertion
  
  Parameters:
  - sat_info: dictionary mapping satellite information to keywords
  """

  insert_sql = """
            INSERT INTO tles(satellite_id, satellite_name, line1, line2, source)
            VALUES (%(sat_id)s, %(sat_name)s, %(line_1)s, %(line_2)s, %(source)s)
            ON CONFLICT(satellite_id)
            DO UPDATE 
            SET line1 = excluded.line1,
                line2 = excluded.line2,
                inserted_at = NOW();
        """
  exec_commit(insert_sql, sat_info)

def list_tles() -> list[dict[str, Any]]:
  """
  Grab All TLEs from the table
  
  Returns: list of tuples containing satellite information and associated tle data
  """

  result_list = []
  tle_rows = exec_get_all("SELECT * FROM tles;")
  for row in tle_rows:
    tle = tuple_to_tle_dict(row)
    result_list.append(tle)
  
  return result_list

def get_tle_by_name(sat_name: str) -> dict[str, Any]:
  """
  Grab record of satellite by satellite name

  Parameters:
  - sat_name: official name of satellite

  Returns: Dictionary representation of desired satellite record
  """
  
  satellite_sql = """
                SELECT *
                FROM tles
                WHERE satellite_name = %(name)s
              """
  satellite_tuple = exec_get_one(satellite_sql, {"name": sat_name})
  return tuple_to_tle_dict(satellite_tuple)