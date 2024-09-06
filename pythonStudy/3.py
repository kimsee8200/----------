import tkinter as tk

root = tk.Tk()
root.title("창2")
root.geometry("1000x100")
label = tk.Label(root,text="이거 냉동이여유?")
label.pack()


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
    
    # 창을 중앙에 배치하기 위해 좌표 계산
x = (screen_width - 1000) // 2
y = (screen_height - 100) // 2
    
    # 창의 위치 설정
root.geometry(f'+{x}+{y}')

radio_var = tk.IntVar()

# 라디오 버튼 추가
radio1 = tk.Radiobutton(root, text="아니, 냉동이 아니다", variable=radio_var, value=1)
radio1.pack()

radio2 = tk.Radiobutton(root, text="냉동이여유~", variable=radio_var, value=2)
radio2.pack()

radio3 = tk.Radiobutton(root, text="몰라!", variable=radio_var, value=3)
radio3.pack()

def on_button_click():
    selected_option = radio_var.get()
    print(f"Selected option: {selected_option}")

# 버튼 추가
button = tk.Button(root, text="Submit", command=on_button_click)
button.pack()

root.mainloop()