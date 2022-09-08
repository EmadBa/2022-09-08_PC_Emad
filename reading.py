import sqlite3

connection = sqlite3.connect("led.db")
cursor = connection.cursor()

sql = "SELECT * FROM LEDstatus"
cursor.execute(sql)


for dsatz in cursor:
    print("ledtime:",dsatz[1], "is_on:",dsatz[2])

connection.close()