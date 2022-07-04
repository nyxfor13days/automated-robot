import time
import serial


class read_data:
    def __init__(self, serial_port):
        ser = serial.Serial(
            port=serial_port,
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )

    def read(self):
        data = self.ser.readline()

        return data


if __name__ == '__main__':
    while True:
        read_data('/dev/ttyS0')
