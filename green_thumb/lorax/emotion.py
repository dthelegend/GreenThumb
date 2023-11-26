import serial
import json

SERIAL_PATH = '/dev/serial/by-id/usb-Arduino__www.arduino.cc__0042_95036303235351909121-if00'

ser = serial.Serial(SERIAL_PATH)
ser.timeout = None

def send_message(sev: int, text: str):
    ser.write(str.encode(sev) + text + '\x00')

def recv_message():
    b = ser.readline()

    print(f"Got message {b}")

    try:
        return json.loads(b)
    except ValueError:
        pass