import serial

try:
    ser = serial.Serial("COM20", 9600)
    ser.timeout = 5000
except Exception:
    print("COM20 not found")
    exit()

direction = "u"
degrees = 30

ser.write(bytearray("%"+direction+"#"+str(degrees)+"&",'ascii'))

ser.close()
