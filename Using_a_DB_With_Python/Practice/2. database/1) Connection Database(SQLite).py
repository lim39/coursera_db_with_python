############################
# 목적: 이메일 카운팅
# Counts 라는 테이블을 생성하여, txt파일을 읽어 email을 가져옴
# email이 테이블에 존재하지 않으면 count = 1 로 인서트하고, 존재한다면 count= count+1로 count컬럼만 갱신
############################
import sqlite3

conn= sqlite3.connect('emaildb.sqlite')
cur= conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts
''')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)
''')

fname= input('Enter file name: ')
if (len(fname)<1): 
    fname = 'mbox-short.txt'
    fh= open(fname)
    for line in fh:
        if not line.startswith('From: '): 
            continue
        pieces= line.split()
        email= pieces[1]
        cur.execute('''SELECT count FROM Counts WHERE email= ?''',(email,))
        row = cur.fetchone()
        if row is None:
            cur.execute('''INSERT INTO Counts (email,count) VALUES(?,1)''',(email,))
        else:
            cur.execute('''UPDATE Counts SET count= count+1 WHERE email= ?''',(email,))
        conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr= '''SELECT email,count FROM Counts ORDER BY count desc'''

for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])

cur.close()
conn.close()