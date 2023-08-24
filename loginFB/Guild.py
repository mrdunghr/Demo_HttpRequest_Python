import threading
import time
import tkinter as tk
from tkinter import messagebox, simpledialog

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def runtest(numberThread):
    print("Đang chạy luồng", numberThread)
    cookies = {
        "1": "sb=7hoRZP_13NByXs2rMIJWnC2m; datr=F4TbZJcqtm9FpbUYljZaAkBi; c_user=100003593851563; xs=12%3An9Q5MJdDf_9NIA%3A2%3A1692690702%3A-1%3A6394%3A%3AAcUSOpc6nQXBlVzo6T7LB9KeYjXkIRlBnHyiiXf-ZQ; fr=0wGTWOUYVHCub7HUt.AWUN27HwPfxiiwd-UzflBtEh0dI.Bk5WyE.f9.AAA.0.0.Bk5XdJ.AWVNmoyehLM; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1692759911723%2C%22v%22%3A1%7D; wd=1920x476",
        "2": "sb=Npe0ZPmXrM4zlgd6cEvyHkvt; datr=Npe0ZCvg0mVr3GZO7A0lxJ6W; c_user=100082516245283; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1692756662389%2C%22v%22%3A1%7D; xs=39%3AEPUThndVv5s7EA%3A2%3A1690247198%3A-1%3A6394%3A%3AAcUpTQNjRt0ZVxX1Z-NafOqPqFXTR9HiBZCOaXjx0HY; fr=0kaThHf1J6EzwQs0q.AWUGNeNLk3zA7OOz5IZ0VPKFwRM.Bk5YGB.Ul.AAA.0.0.Bk5YGB.AWV4jCKY3n4; wd=1920x608"
    }
    choice = input("Nhập 1 hoặc 2: ")
    if choice in cookies:
        cookie = cookies[choice]
    else:
        print("Lựa chọn sai. Vui lòng nhập lại.")

    driver = webdriver.Chrome(service=Service(executable_path="../vevn/chromedriver.exe"))
    driver.get("https://fb.com/")
    script = (
            'javascript:void(function(){ function setCookie(t) { var list = t.split("; "); console.log(list); '
            'for (var i = list.length - 1; i >= 0; i--) { var cname = list[i].split("=")[0]; var cvalue = list[i].split("=")[1]; '
            'var d = new Date(); d.setTime(d.getTime() + (7*24*60*60*1000)); var expires = ";domain=.facebook.com;expires="+ d.toUTCString(); '
            'document.cookie = cname + "=" + cvalue + "; " + expires; } } function hex2a(hex) { var str = ""; for (var i = 0; i < hex.length; i += 2) '
            '{ var v = parseInt(hex.substr(i, 2), 16); if (v) str += String.fromCharCode(v); } return str; } '
            'setCookie("' + cookie + '"); location.href = "https://facebook.com"; })();')

    driver.execute_script(script)

    x = numberThread * 400
    y = 10
    driver.set_window_rect(x, y, 400, 600)
    time.sleep(1000)
    driver.quit()


def start_new_thread():
    cookie_choice = simpledialog.askstring("Lựa chọn cookie", "Nhập lựa chọn (1 hoặc 2):")
    if cookie_choice == "1" or cookie_choice == "2":
        thread_id = len(arrThread) + 1
        thread = threading.Thread(target=runtest, args=(thread_id, cookie_choice))
        arrThread.append(thread)
        thread.start()
    else:
        messagebox.showerror("Lỗi", "Lựa chọn không hợp lệ. Vui lòng chọn lại.")


def show_running_threads():
    running_threads = "\n".join([f"Luồng {idx + 1}" for idx in range(len(arrThread))])
    messagebox.showinfo("Danh sách các luồng đang chạy", running_threads)


def stop_threads():
    for thread in arrThread:
        thread.join()
    root.destroy()


arrThread = []

root = tk.Tk()
root.title("Quản lý luồng")

start_button = tk.Button(root, text="Khởi động luồng mới", command=start_new_thread)
start_button.pack(pady=10)

show_button = tk.Button(root, text="Xem danh sách các luồng", command=show_running_threads)
show_button.pack(pady=10)

stop_button = tk.Button(root, text="Dừng chương trình", command=stop_threads)
stop_button.pack(pady=10)

root.mainloop()
