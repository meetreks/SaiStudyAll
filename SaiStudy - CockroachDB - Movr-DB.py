import psycopg2
import psycopg2.errorcodes
import time
import logging
import random
dsn = 'postgresql://root@localhost:26257/movr?sslmode=disable'
conn = psycopg2.connect(dsn)

#with conn.cursor as cur:
cur = conn.cursor()
cur.execute("SELECT id, city FROM rides WHERE city in('washington dc')")
rows = cur.fetchall()
conn.commit()
for row in rows:
    print([str(cell)for cell in row])
conn.close()
