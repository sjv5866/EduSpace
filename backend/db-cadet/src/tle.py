from src.db_utils import exec_sql_file

def buildTable():
  """Create the tables to initialize the db"""
  exec_sql_file("schema/schema.sql")