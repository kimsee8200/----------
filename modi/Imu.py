import modi_plus
import time

modules = modi_plus.MODIPlus()

imu = modules.imus[0]
led = modules.leds[0]

try:
  while True:
    print("--------------------")
    print({imu.acceleration}) # 가속도 x = 옆으로 흔들때, y = 세워서 위아래로 흔들때, z = 눞혀서 위아래 ? 
    print({imu.angular_velocity}) #속도 값
    print({imu.angle}) # 각도 x = 위아래 기울기 y = 양옆 기울기 z = 돌리기 각도.

    if(imu.acceleration[1]>=100):
      led.set_rgb(255,000,000)
    else:
      led.turn_off()

    time.sleep(0.1)
except KeyboardInterrupt:
  print("stop the program")