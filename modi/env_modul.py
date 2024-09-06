import modi_plus
import time

modules = modi_plus.MODIPlus()

env_module = modules.envs[0]
led_module = modules.leds[0]

try:
  while True:
    print("-------------")
    print(env_module.temperature) #온도
    print(env_module.humidity) #습도
    print(env_module.intensity) #빛
    print(env_module.volume) #목소리

    if(env_module.volume>=10):
      print("오옹 나이스")
      led_module.set_rgb(255,000,255)
    else:
      led_module.turn_off()

    time.sleep(1)
except KeyboardInterrupt:
  print("stop this program")