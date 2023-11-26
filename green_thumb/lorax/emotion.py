import serial
import json

SERIAL_PATH = '/dev/serial/by-id/usb-Arduino__www.arduino.cc__0042_95036303235351909121-if00'

ser = serial.Serial(SERIAL_PATH)

def send_message(sev: int, text: str):
    ser.write(str.encode(sev) + text + '\0')

def recv_message():
    b = ser.read_until(b'\x00', timeout=None)

    try:
        return json.loads(b)
    except ValueError:
        pass