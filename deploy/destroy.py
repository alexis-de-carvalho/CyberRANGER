import sqlite3
import sys

instance_id = sys.argv[1]
DB_URL = sys.argv[2]

conn = sqlite3.connect(DB_URL)
cursor = conn.cursor()

sql = '''DELETE FROM instances WHERE id = ?'''

cursor.execute(sql, (instance_id,))
conn.commit()
conn.close()