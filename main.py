from gpiozero import LED, Button
from datetime import datetime as DateTime
import sqlite3, os, time
from time import sleep

verbindung = sqlite3.connect('led.db')
zeiger = verbindung.cursor()


db_creat = """
CREATE TABLE IF NOT EXISTS LEDstatus(
Lid INTEGER PRIMARY KEY,
ledtime TIMESTAMP,
is_on BOOL
)
"""
zeiger.execute(db_creat)
verbindung.commit()

class LED(LED):
    def __init__(self,pin):
        super().__init__(pin)
        self.check = None
        
    def toggle(self):
        super().toggle()
        self.check = False
        
        
button = Button(23)
led = LED(24)

button.when_pressed = led.toggle

while True:
    if led.check == False:
        zeit = DateTime.now()
        time = zeit.strftime('%H:%M:%S')
        if led.value == 1:
            status = "TRUE"
        else:
            status = "FALSE"
        zeiger.execute("""INSERT INTO LEDstatus (ledtime,is_on) VALUES(?,?)""",[time,status])
        verbindung.commit()
        led.check = True
        
verbindung.commit()
verbindung.close()