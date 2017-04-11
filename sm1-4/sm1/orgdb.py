import sqlite3
import re

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: ') : continue
    # Your code there
    g = str(re.findall(r'@(\w.+)',line.split()[1]))

    # Get domain name - org variable
    print g
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (g, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count) 
                VALUES ( ?, 1 )''', ( g, ) )
    else : 
        cur.execute('UPDATE Counts SET count=count+1 WHERE email = ?', 
            (g, ))
    # This statement commits outstanding changes to disk each 
    # time through the loop - the program can be made faster 
    # by moving the commit so it runs only after the loop completes
    conn.commit()

# https://www.sqlite.org/lang_select.html
# Your code there
# Make your sql request - get top 10 rows ordered by count
# sqlstr = 'SELECT ... '
sqlstr = 'SELECT email,count FROM Counts ORDER BY count DESC LIMIT 10'
print
print "Counts:"
for row in cur.execute(sqlstr) :
    # Your code there
    print str(row[0]),str(row[1])

cur.close()

