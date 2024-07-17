import sqlite3
import sys

network = sys.argv[1]
network_ip = sys.argv[2]
instance_id = sys.argv[3]
DB_URL = sys.argv[4]

conn = sqlite3.connect(DB_URL)
cursor = conn.cursor()

sql = '''UPDATE instances
         SET network = ?, ip = ?, status = ?
         WHERE id = ?'''

cursor.execute(sql, (network, network_ip, "RUNNING", instance_id))
conn.commit()
conn.close()