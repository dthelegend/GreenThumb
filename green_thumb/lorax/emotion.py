import serial
import json

SERIAL_PATH = '/dev/serial/by-id/usb-Arduino__www.arduino.cc__0042_95036303235351909121-if00'

ser = serial.Serial(SERIAL_PATH)
ser.timeout = None

def send_message(sev: int, text: str):
    ser.write(sev.to_bytes(1, 'big') + bytes(text, encoding='utf-8') + b'\x00')

def recv_message():
    b = ser.readline()

    try:
        return json.loads(b)
    except ValueError:
        print(f"Failed to load message {b}")