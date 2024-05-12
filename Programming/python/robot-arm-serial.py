import serial

ser = serial.Serial("COM6", 9600)

# Raise the robot arm a tiny bit
ser.write(bytearray('%4#', 'ascii'))
