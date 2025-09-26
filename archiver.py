# Archiver python program
# This program simply reads the exporte Onetab txt file and stores in an on-disk database.
import sqlite3
from datetime import datetime

# class Archive:
#     def __init__(self):
#         self.links = {}

# archive = Archive()

links = {}
for line in (open('links.txt')):
    tokens = line.split('|')
    if len(tokens) >= 2:
        url = tokens[0].strip()
        title = tokens[1].strip()
        links[url] = {
            'title': title,
            'tags': [],
            'added_on': datetime.now(),
            'domain': url.split('//')[1].split('/')[0]
        }

print("-----------------------------------------------------")
print("- Initializing archival database...")

con = sqlite3.connect("web-archive.db")
# Meant for when you want to interact with rows.
# con.row_factory = sqlite3.Row
cur = con.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS links (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT NOT NULL,
        title TEXT NOT NULL,
        tags TEXT NULL,
        added_on DATETIME NOT NULL,
        domain TEXT NOT NULL
    )
''')


print("- Checking database and table creation...")
res = cur.execute("SELECT name FROM sqlite_master")
if(res.fetchone() is None):
    print("Table creation failed.")
    exit()

print("- Preparing data for insertion...")
for url in links:
    link = links[url]
    cur.execute('''
        INSERT INTO links (url, title, tags, added_on, domain)
        VALUES (?, ?, ?, ?, ?)
    ''', (url, link['title'], ', '.join(link['tags']), link['added_on'], link['domain']))

print("- Feeding data into the table...")
con.commit()

conf = cur.execute("SELECT * FROM links")
print("-----------------------------------------------------")
if(conf.fetchone() is None):
    print("No data inserted.")
    exit()
print("- Printing a single row for verification: ")
print(conf.fetchone())
print("-----------------------------------------------------")
print("Done.")


# Code for printing all in a table
#
# row = cur.fetchone()
# cols = row.keys()

# rows = cur.fetchall()
# print(" | ".join(cols))
# for row in rows:
#     print("-" * (len(" | ".join(cols))))
#     print(" | ".join(str(row[col]) for col in cols))

# print(" | ".join(str(row[col]) for col in cols))
