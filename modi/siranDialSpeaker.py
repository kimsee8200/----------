import modi_plus
import time

modules = modi_plus.MODIPlus()

dial = modules.dials[0]
speaker = modules.speakers[0]



try:
  while True:
    # 517 = do
    # 500 부터 먹힘.
    # 기존 주파수*2 = speaker의 주파수.
    print(dial.turn)
    speaker.set_tune(550+dial.turn,dial.turn)
    # speaker.set_tune(261, dial.turn)
    time.sleep(0.1)

except KeyboardInterrupt:
  speaker.set_tune(0,0)
  print("stop the program")