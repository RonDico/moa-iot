from gpiozero import LED, Button

led = LED(4)
button = Button(22)

led.on()
button.when_pressed = led.off
button.when_released = led.on
