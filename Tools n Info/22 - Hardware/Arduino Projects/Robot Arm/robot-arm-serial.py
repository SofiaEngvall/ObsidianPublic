import serial

delay = 2

try:
    ser = serial.Serial("COM20", 9600)
    ser.timeout = 5000
except Exception:
    print("COM20 not found")
    exit()
print("Connected to serial")

direction = "l"
degrees = 30

ser.write(bytearray("%"+direction+"#"+str(degrees)+"&",'ascii'))

direction = "r"
degrees = 50

ser.write(bytearray("%"+direction+"#"+str(degrees)+"&",'ascii'))

ser.close()
