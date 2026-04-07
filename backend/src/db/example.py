import os
from .db_utils import *

def rebuild_tables():
    exec_sql_file('src/db/schema.sql')

def list_examples():
    return exec_get_all('SELECT * FROM tle')