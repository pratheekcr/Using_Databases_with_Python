import sqlite3

conn = sqlite3.connect('week2_2.sqlite')
cur = conn.cursor()

cur.execute(''' DROP TABLE  IF EXISTS Counts''')

cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = 'mbox.txt'
fhand = open(fname)
for line in fname:
    if not line.startswith('From:'): continue
    pieces = line.split()
    org1 = pieces[1]
    apos = org1.find('@')
    org = org1[apos + 1:]
    cur.execute('SELECT count FROM Counts WHERE org = ?',(org,))
    if row is not None:
        for row in cur:
            cur.execute('''INSERT INTO Counts (org,count) VALUES (?,1)''',(org,))
    else:
        cur.execute('UPDATE Counts SET count=count+1 WHERE org =?',(org,))
conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0], row[1]))

cur.close()