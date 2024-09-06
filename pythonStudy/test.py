import modi_plus
from PIL import Image

# MODI+ 모듈 초기화
bundle = modi_plus.MODIPlus()

# 디스플레이 모듈 가져오기
display = bundle.displays[0]

# 이미지를 디스플레이 모듈로 전송
display.draw_picture(0,0,"Train")

# 이미지 표시
display.show()
