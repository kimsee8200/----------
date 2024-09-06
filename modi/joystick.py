import modi_plus
import time

modules = modi_plus.MODIPlus()
joystick = modules.joysticks[0]

try:
  while True:
    print("--------")
    print(joystick.direction)
    print(joystick.x)
    print(joystick.y)
    time.sleep(0.5)
except KeyboardInterrupt:
  print("stop the program")