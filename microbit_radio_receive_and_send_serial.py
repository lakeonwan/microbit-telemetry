from microbit import *
import radio

radio.on()
# radio.config(power=6)
# radio.config(channel=19)

data_request_command = "data_request"
sleep_time_after_receiving = 5000
sleep_time_inner_loop = 1000

display.show("R")
sleep(200)
display.clear()

while True:
    print("sending command: {}".format(data_request_command))
    radio.send(data_request_command)
    msg = radio.receive()
    print("radio received: {}".format(msg))
    if msg:
        print("radio received data")
        print(msg)
        display.set_pixel(2,2,1)
        sleep(100)
        display.clear()
        print("sleeping after radio receive and serial print for {}".format(sleep_time_after_receiving))
        sleep(sleep_time_after_receiving)
    sleep(sleep_time_inner_loop)
