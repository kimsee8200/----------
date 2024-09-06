import tkinter as tk
from tkinter import messagebox
import modi_plus as md
import time

# MODIPlus 모듈 초기화
bundle = md.MODIPlus()
speaker = bundle.speakers[0]

# 각 음의 이름과 주파수 설정 (Hz 단위)
notes = {
    '도': 261,     # C4
    '레': 293,     # D4
    '미': 329,     # E4
    '파': 349,     # F4
    '솔': 392,     # G4
    '라': 440,     # A4
    '시': 493,     # B4
    '도 (고음)': 523 # C5
}

def play_note(note):
    """스피커로 음을 재생합니다."""
    frequency = notes.get(note)
    #print(speaker.preset_musics())
    if frequency:
        speaker.set_tune(frequency,100)  # 주파수 설정
        #speaker.play_music(frequency,50)  # 음 재생
        time.sleep(0.5)  # 음 재생 후 잠시 대기
        speaker.stop_music()  # 음 정지

# 메인 윈도우 생성
root = tk.Tk()
root.title("피아노")

# 윈도우 크기 설정
root.geometry("750x300")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
    
    # 창을 중앙에 배치하기 위해 좌표 계산
x = (screen_width - 1000) // 2
y = (screen_height - 100) // 2
    
    # 창의 위치 설정
root.geometry(f'+{x}+{y}')

# 각 버튼 생성 및 배치
for note in notes:
    button = tk.Button(root, text=note, command=lambda n=note: play_note(n), width=10, height=4)
    button.pack(side=tk.LEFT, padx=5, pady=5)

# 메인 루프 시작
root.mainloop()
