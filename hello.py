import MySQLdb

conn = MySQLdb.connect(
    host="sql6.freemysqlhosting.net",
    port=3306,
    user="sql6424443",
    password="YYBPDNQbM3",
    database="sql6424443"
)
c = conn.cursor()

print(conn)