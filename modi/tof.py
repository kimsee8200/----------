import modi_plus
import time

modules = modi_plus.MODIPlus()

tof = modules.tofs[0]
leds = modules.leds[0]

try:
  while True:
    print(tof.distance)
    if(tof.distance>0):
      leds.turn_on()
      leds.set_rgb(tof.distance,000,000)
    else:
      leds.turn_off()
    time.sleep(0.1)

except KeyboardInterrupt:
  leds.turn_off()
  print("stop the program")