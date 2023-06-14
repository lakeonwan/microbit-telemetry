import serial
import signal
import time
import datetime


# hub code read from serial port and process data
# MacOs Micro:Bit device --> /dev/cu.usbmodem1441402 115200
# Rpi Micro:Bit device --> ls /dev/ttyACM*


def handler(signum, frame):
    exit(0)


signal.signal(signal.SIGINT, handler)

while True:
    timeout_in_seconds = 7
    with serial.Serial('/dev/ttyACM0', 115200, timeout=timeout_in_seconds) as ser:
        x = ser.read_until()
        print('{}'.format(x))
        # with open('telemetry.log', 'ab') as a_writer:
        # a_writer.write(x)
        with open('telemetry.log', 'a') as a_writer:
            now = datetime.datetime.now()
            a_writer.write("{} {}".format(now.strftime("%Y-%m-%d %H:%M:%S"), str(x, 'utf-8')))

    time.sleep(1)
