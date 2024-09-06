import tkinter as tk
import modi_plus as md

button_state = "On"

root = tk.Tk()
root.title("버튼 예제")

root.geometry("300x200")
label = tk.Label(root,text="이거 냉동이여유?")
label.pack()


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
    
    # 창을 중앙에 배치하기 위해 좌표 계산
x = (screen_width - 300) // 2
y = (screen_height - 200) // 2
    
    # 창의 위치 설정
root.geometry(f'+{x}+{y}')

bundle = md.MODIPlus()
led = bundle.leds[0]
display = bundle.displays[0]



new_brightness = 0


def adjust_brightness(increase):
    global new_brightness
    """LED 밝기를 조절합니다."""
    if increase:
        new_brightness = min(new_brightness + 10, 100)  # 최대 밝기 100으로 제한
        display.text = "Up"
    else:
        new_brightness = max(new_brightness - 10, 10)  # 최소 밝기 0으로 제한
        display.text = "Down"

    led.set_rgb(new_brightness,new_brightness,new_brightness)  # 새 밝기로 설정
    print(f"현재 밝기: {new_brightness}")

def on_up_button_click():
    print("↑ 화살표 버튼 클릭됨")
    adjust_brightness(increase=True)

def on_down_button_click():
    print("↓ 화살표 버튼 클릭됨")
    adjust_brightness(increase=False)

def on_on_button_click():
    global button_state
    if button_state == "On":
        led.turn_on()
        display.text = "On"
        button_state = "Off"
        button.config(text="Off")
    else:
        led.turn_off()
        display.text = "Off"
        button_state = "On"
        button.config(text="On")
    print("On 버튼 클릭됨")
    


# ↑ 화살표 버튼
up_button = tk.Button(root, text="↑", command=on_up_button_click)
up_button.pack(side=tk.TOP, pady=10)

# ↓ 화살표 버튼
down_button = tk.Button(root, text="↓", command=on_down_button_click)
down_button.pack(side=tk.TOP, pady=10)

# On 버튼
button = tk.Button(root, text="On", command=on_on_button_click)
button.pack(side=tk.TOP, pady=10)


# 메인 루프 시작
root.mainloop()