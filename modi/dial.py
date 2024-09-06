import modi_plus
import time

modules = modi_plus.MODIPlus()

dial = modules.dials[0]

try:
  while True:
    print("-------")
    print(dial.speed) 
    print(dial.turn)
    time.sleep(0.5)
except KeyboardInterrupt:
  print("stop the program")



