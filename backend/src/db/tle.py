from .db_utils import exec_get_all
from typing import Optional, Iterable, Dict, Tuple, Any

def tupleToTLE(tle: Tuple[int, int, str, str, str, Any, str, Any]) -> Dict[str, Any]:
  id, satelliteId, name, line1, line2, epoch, source, inserted = tle
  return {
    "id": id,
    "satelliteId": satelliteId,
    "name": name,
    "line1": line1,
    "line2": line2,
    "epoch": str(epoch),
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
