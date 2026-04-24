from .db_utils import exec_get_all
from typing import Optional, Iterable, Dict, Tuple, Any

def tupleToTLE(tle: Tuple[int, int, str, str, str, Any]) -> Dict[str, Any]:
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

def listTLES():
  """Grab All TLEs from the table"""
  result_list = []
  tle_rows = exec_get_all("SELECT * FROM tles;")
  for row in tle_rows:
    tle = tupleToTLE(row)
    result_list.append(tle)
  
  return result_list

def insertTLES(sat_id: int, sat_name: str, line_1: str, line_2: str):
  """
  Propagates TLE to Postgres database
  sat_id: catalog number associated with satellite
  sat_name: official satellite name
  line_1: first line in TLE object
  line_2: second line in TLE object
  """

  insert_sql = """
    INSERT INTO tles(id, satellite_id, satellite_name, line1, line2)
    VALUES (1, 1, 'TEST', 'LINE 1', 'LINE 2', NOW())
    ON CONFLICT(id)
    DO UPDATE SET 
        inserted_at = NOW();
  """
