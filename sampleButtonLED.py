from gpiozero import LED, Button

led = LED(4)
button = Button(22)

while True:
    if button.is_pressed:
        led.off()
    else:
        led.on()
        