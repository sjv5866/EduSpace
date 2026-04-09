import os
from .db_utils import *

def list_examples():
    return exec_get_all('SELECT * FROM tles;')