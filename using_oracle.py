import cx_oracle

tsn = cx_oracle.make_tsn(....)

conn = cx_oracle.connect('user', 'p/w', tsn)

cursor = conn.cursor()

cursor.execute('select foo from bar')

for row in cursor.fetchall():
    print(row)

conn.close()
