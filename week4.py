import urllib.request, urllib.parse
import sqlite3
import json

conn = sqlite3.connect('week4db.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;
''')

cur.executescript('''
CREATE TABLE User (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
name TEXT
);

CREATE TABLE Course(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
title TEXT
);

CREATE TABLE Member(
user_id INTEGER,
course_id INTEGER,
role INTEGER,
PRIMARY KEY (user_id, course_id)
)
''')

fname = 'roster_data.json'

fhand = open(fname)
data = fhand.read()
js = json.loads(data)
print(json.dumps(js))
for line in js:
    user = line[0]
    course = line[1]
    role = line[2]

    if user is None or course is None or role is None: continue

    cur.execute('''INSERT INTO User (name) VALUES (?)''', (user,))
    cur.execute('''SELECT id FROM User WHERE name =?''', (user,))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT INTO Course (title) VALUES (?)''', (course,))
    cur.execute('''SELECT id FROM Course WHERE title=?''', (course,))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT INTO Member (user_id, course_id, role) VALUES (?, ?, ?)''', (user_id, course_id, role))
    conn.commit()