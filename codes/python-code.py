import serial
import time

'''
    this code is just for one led (pin 13 atmega328 (arduino))
    but there is 9 more I/O's to control. (code is just like below)
'''

# COM4 is the port name for my pc usb port
ser = serial.Serial('COM4', 9600, timeout=0.05)   #for conecting devises

if not ser.isOpen():
    ser.open()
print('ready .... com is open')
time.sleep(1)

line = ser.readline()
print(line)
print('commands are: on, off, exit.')

while ser.is_open :
    inp = input('commands to make system on and off : ')
    print('you entered : ', inp)

    if (inp == 'on'):
        ser.write(str.encode('1'))
        print('LED ON')
    if (inp == 'off'):
        ser.write(str.encode('0'))
        print('LED OFF')
    if (inp == 'exit'):
        ser.write(str.encode('0'))
        print('close serial port')
        ser.close()
        
