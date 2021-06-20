# WaveShapePlay
# Find a detailed youtube tutorial for the Arduino Com Connection Code at: https://youtu.be/DJD28uK5qIk

import serial.tools.list_ports
commPort = 'None'

ports = serial.tools.list_ports.comports()
numConnection = len(ports)
    
for i in range(0,numConnection):
    port = ports[i]
    strPort = str(port)

    if 'CH340' in strPort:
        splitPort = strPort.split(' ')
        commPort = (splitPort[0])

if commPort != 'None':
    ser = serial.Serial(commPort,baudrate = 9600, timeout=1)
    print('Connected to ' + commPort)

else:
    print('Connection Issue!')

print('DONE')
