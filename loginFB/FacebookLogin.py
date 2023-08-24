from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class FacebookLogin:
    def __init__(self):
        self.driver = None
        self.cookies = {
            "1": "sb=7hoRZP_13NByXs2rMIJWnC2m; datr=F4TbZJcqtm9FpbUYljZaAkBi; c_user=100003593851563; xs=12%3An9Q5MJdDf_9NIA%3A2%3A1692690702%3A-1%3A6394%3A%3AAcUSOpc6nQXBlVzo6T7LB9KeYjXkIRlBnHyiiXf-ZQ; fr=0wGTWOUYVHCub7HUt.AWUN27HwPfxiiwd-UzflBtEh0dI.Bk5WyE.f9.AAA.0.0.Bk5XdJ.AWVNmoyehLM; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1692759911723%2C%22v%22%3A1%7D; wd=1920x476",
            "2": "sb=Npe0ZPmXrM4zlgd6cEvyHkvt; datr=Npe0ZCvg0mVr3GZO7A0lxJ6W; c_user=100082516245283; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1692756662389%2C%22v%22%3A1%7D; xs=39%3AEPUThndVv5s7EA%3A2%3A1690247198%3A-1%3A6394%3A%3AAcUpTQNjRt0ZVxX1Z-NafOqPqFXTR9HiBZCOaXjx0HY; fr=0kaThHf1J6EzwQs0q.AWUGNeNLk3zA7OOz5IZ0VPKFwRM.Bk5YGB.Ul.AAA.0.0.Bk5YGB.AWV4jCKY3n4; wd=1920x608"
        }

    def login(self):
        while True:
            choice = input("Nhập 1 hoặc 2: ")
            if choice in self.cookies:
                cookie = self.cookies[choice]
                break
            else:
                print("Lựa chọn sai. Vui lòng nhập lại.")

        self.driver = webdriver.Chrome(service=Service(executable_path="../vevn/chromedriver.exe"))
        self.driver.get("https://fb.com/")

        script = (
                'javascript:void(function(){ function setCookie(t) { var list = t.split("; "); console.log(list); '
                'for (var i = list.length - 1; i >= 0; i--) { var cname = list[i].split("=")[0]; var cvalue = list[i].split("=")[1]; '
                'var d = new Date(); d.setTime(d.getTime() + (7*24*60*60*1000)); var expires = ";domain=.facebook.com;expires="+ d.toUTCString(); '
                'document.cookie = cname + "=" + cvalue + "; " + expires; } } function hex2a(hex) { var str = ""; for (var i = 0; i < hex.length; i += 2) '
                '{ var v = parseInt(hex.substr(i, 2), 16); if (v) str += String.fromCharCode(v); } return str; } '
                'setCookie("' + cookie + '"); location.href = "https://facebook.com"; })();')

        self.driver.execute_script(script)

    def close(self):
        if self.driver is not None:
            self.driver.quit()
