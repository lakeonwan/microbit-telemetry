from microbit import *
import radio

radio.on()
# radio.config(power=6)
# radio.config(channel=19)
display_enabled = False
sleep_time_after_send = 5000
sleep_time_inner_loop = 1000
data_request_command = "data_request"

display.show("S")
sleep(200)
display.clear()

while True:
    t = temperature()
    l = display.read_light_level()
    s = microphone.sound_level()

    print("sensing: t:{};l:{};s:{};".format(t, l, s))

    msg = radio.receive()
    if msg == data_request_command:
        print("incoming command: {}".format(msg))
        print("radio send: t:{};l:{};s:{};".format(t, l, s))
        radio.send("t:{};l:{};s:{};".format(t, l, s))
        print("sleeping after radio send for {}".format(sleep_time_after_send))
        sleep(sleep_time_after_send)

    if button_a.is_pressed():
        if display_enabled:
            display_enabled = False
            display.clear()
        else:
            display_enabled = True

    if display_enabled:
        display.set_pixel(0, 0, 9 * t // 50 if t >= 0 else 0)
        display.set_pixel(1, 0, 9 * l // 255)
        display.set_pixel(2, 0, 9 * s // 255)

    sleep(sleep_time_inner_loop)
