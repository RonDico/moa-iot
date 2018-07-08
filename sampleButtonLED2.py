from gpiozero import LED, Button

led = LED(4)
button = Button(22)

while True:
    button.wait_for_press()
    led.off()
    button.wait_for_release()
    led.on()
    