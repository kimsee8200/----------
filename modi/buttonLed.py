import modi_plus
import time

bundle = modi_plus.MODIPlus()
button = bundle.buttons[0]
led = bundle.leds[0]
led_on = False

try:
  while True:
    if button.clicked:
      led_on = not led_on
      if led_on:
        led.set_rgb(255,000,000)
        led.turn_on()
      else:
        led.turn_off()
    if button.double_clicked:
      print("따블끌릭")
    if button.pressed:
      print("프레쓰")
    if button.toggled:
      print("또글")
    time.sleep(0.2)

except KeyboardInterrupt:
  led.set_rgb(0,0,0)
  print("종료")