import serial
import time

try:
    ser = serial.Serial("COM16", 9600)
except Exception:
    print("COM16 not found")
    exit()

for x in range(6):
    ser.write(bytearray('%4#', 'ascii'))
    time.sleep(1)
for x in range(6):
    ser.write(bytearray('%7#', 'ascii'))
    time.sleep(1)

for x in range(6):
    ser.write(bytearray('%5#', 'ascii'))
    time.sleep(1)
for x in range(6):
    ser.write(bytearray('%6#', 'ascii'))
    time.sleep(1)

for x in range(6):
    ser.write(bytearray('%A#', 'ascii'))
    time.sleep(1)
for x in range(6):
    ser.write(bytearray('%D#', 'ascii'))
    time.sleep(1)

for x in range(6):
    ser.write(bytearray('%B#', 'ascii'))
    time.sleep(1)
for x in range(6):
    ser.write(bytearray('%C#', 'ascii'))
    time.sleep(1)

# input("Press any key")
