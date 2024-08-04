import tkinter as tk

import threading


# Tạo cửa sổ chính
root = tk.Tk()

root.title("Tkinter GUI Example")
root.geometry("1200x750")  # Tăng kích thước cửa sổ để phù hợp với các textbox rộng và cao hơn

# Tạo frame để sắp xếp các nhãn và ô nhập liệu
frame = tk.Frame(root)
frame.pack(pady=10)

# Kích thước chữ
label_font = ("Arial", 14)
button_font = ("Arial", 14)
# tieu de
notification_label = tk.Label(root, text='''text
                              '''
                              , fg="red", font=("Arial", 12))
notification_label.pack(pady=10)
t=0
import time
def update_notification():
    global t, updating
    while updating:
        t += 1
        time.sleep(0.1)
        notification_label.config(text=f"Số lần: {t}")
        # Gọi update_idletasks để cập nhật GUI ngay lập tức
        root.update_idletasks()
    notification_label.config(text="Đã ấn stop")
def start_update():
    global updating
    updating = True
    th = threading.Thread(target=update_notification)
    th.setDaemon(True)
    th.start()

# Hàm để dừng cập nhật
def stop_update():
    global updating
    updating = False
    notification_label.config(text=f"Đã ấn stop")

def preprocess():
    notification_label.config(text="Start")

    start_update()
start_button = tk.Button(root, text="Start", font=button_font, command=preprocess)
start_button.pack(pady=10)

# Tạo nút dừng (Stop button)
stop_button = tk.Button(root, text="Stop", font=button_font, command=stop_update)
stop_button.pack(pady=10)

root.mainloop()

