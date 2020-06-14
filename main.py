import sqlite3
from config import CONNECTION_STRING

conn = sqlite3.connect(CONNECTION_STRING)
c = conn.cursor()

