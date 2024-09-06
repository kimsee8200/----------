import modi_plus
import time  # 시간을 제어하기 위해 time 모듈을 import합니다.
bundle = modi_plus.MODIPlus()

# 스피커 모듈 가져오기
speaker = bundle.speakers[0]

# 음계 주파수 (Hz)
NOTES = {
    'do': 261*2,  # C4
    're': 293*2,  # D4
    'mi': 329*2,  # E4
    'fa': 349*2,  # F4
    'sol': 392*2, # G4
    'la': 440*2,  # A4
    'si': 493*2,  # B4
    'do_high': 523*2  # C5 (높은 도)
}

speaker.SCALE_TABLE = NOTES

# 음을 연주하는 함수
def play_tone(note, duration):
    frequency = NOTES[note]
    speaker.set_tune = (frequency, duration)  # 주파수와 지속 시간을 튜플로 전달
    time.sleep(duration)
    #speaker.set_tune = (0, 0)  # 음을 끄기 위해 주파수와 시간을 0으로 설정
    #time.sleep(0.2)  # 음 사이의 간격

try:
    while True:
        # 도레미파솔라시도 연주
        play_tone('do', 100)
        play_tone('re', 100)
        play_tone('mi', 100)
        play_tone('fa', 100)
        play_tone('sol', 100)
        play_tone('la', 100)
        play_tone('si', 100)
        play_tone('do_high', 100)

except KeyboardInterrupt:
    print("연주가 중지되었습니다.")