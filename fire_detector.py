from gpio import *
from time import *
def handleSensorData():
value = digitalRead(0)
if value == 0:
customWrite(1, '0')
else:
customWrite(1, '1')
def main():
add_event_detect(0, handleSensorData)
while True:
delay(1000)
if name == " main ":
main()