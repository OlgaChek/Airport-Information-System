import sqlite3
import io

conn = sqlite3.connect('database.db')

with io.open('dump.sql', 'w') as f:
    for line in conn.iterdump():
        f.write('%s\n' % line)

conn.close()