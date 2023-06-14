# microbit-telemetry

This project uses two BBC micro:bits and one computer

## micro:bit v2 - sensor and transmitter (radio)

[microbit_sense_and_send.py](microbit_sense_and_send.py)

When the application is started, the micro:bit screen shows the letter 'S'.

After that it periodically senses:

- temperature
- light level 
- sound level using micro:bit v2 build-in microphone

When pressing button A, the micro:bit led screen outputs sensor data

- The first led brightness corresponds with temperature
- The second led brightness corresponds with light level 
- The third led brightness corresponds with sound level

Pressing button A again disables outputting to the led screen

## micro:bit - receiver (radio) and transmitter (serial)
[microbit_radio_receive_and_send_serial.py](microbit_radio_receive_and_send_serial.py)

When the application is started, the micro:bit screen shows the letter 'R'.

After that it  periodically checks for incoming data that is sent by the sensor micro:bit v2.
When data is received, a led on the led screen is turned on briefly

## computer - receiver (serial) and logger
[hub_serial_read_and_process.py](hub_serial_read_and_process.py)

This application receives its telemetry data over the serial port and logs it in a file called telemetry.log

The serial port settings are:

| setting  |     value      |
|:---------|:--------------:|
| port     | `/dev/ttyACM0` |
| baudrate |     115200     |
