import serial
import json

SERIAL_PATH = ""

ser = serial.Serial(SERIAL_PATH)

def send_message(sev: int, text: str):
    ser.write(bytes(sev) + bytes(text))

def recv_message():
    b = ser.read_until('\0')

    try:
        return json.loads(b)
    except ValueError:
        pass