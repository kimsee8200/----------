import modi_plus
import io
import time
from PIL import Image

image = Image.open("C:/Users/user/Downloads/nikita.jpg")

byte = io.BytesIO()
image.save(byte, format='JPEG')

image_byte = byte.getvalue()

modules = modi_plus.MODIPlus()
display = modules.displays[0]
x = 0
y = 0

#display.draw_picture(x,0,"Apartment")
#display.write_variable(x,y,1917.1981)
display.draw_dot(image_byte)

flag = True

try:
  while True:
    while x<16: # 16이 한 바퀴.
      x=x+1
      display.move_screen(x,0)
      time.sleep(0.1)
    while x>0:
      x=x-1
      display.move_screen(x,0)
      time.sleep(0.1)
    # if flag:
    #   display.write_text("Dynamic     Busan")
    # else:
    #   display.write_text("87         국민근린공원 -> 중암동")
    time.sleep(1)
    # flag = not flag
    
    

except KeyboardInterrupt:
  print("stop this progrem")
