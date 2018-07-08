from gpiozero import *
from time import sleep

out = OutputDevice(17)
button = Button(22)

out.on()

while True:
    if button.is_pressed:
        out.off()
    else:
        out.on()
    sleep(1)

