import requests


class ApiFacebook:
    # def __int__(self, cookie) -> None:
    def __init__(self) -> None:
        self.header = {
            "authority": "www.facebook.com",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "vi",
            "Cache-Control": "max-age=0",
            "Cookie": 'sb=7hoRZP_13NByXs2rMIJWnC2m; datr=F4TbZJcqtm9FpbUYljZaAkBi; c_user=100003593851563; xs=12%3An9Q5MJdDf_9NIA%3A2%3A1692690702%3A-1%3A6394%3A%3AAcX49MsQUXdbZWkMTDAJhDvIQBrc6F7-SF9f7483fg; fr=0Ehc0lXalOPxHF9gF.AWXMJIXCCCR8SalI39yUh8GQ6dU.Bk5cZ0.f9.AAA.0.0.Bk5cal.AWUExrXU_Lw; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1692780223223%2C%22v%22%3A1%7D; wd=1920x444',
            "Dpr": "1",
            "Sec-Ch-Prefers-Color-Scheme": "dark",
            "Sec-Ch-Ua": 'Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            "Sec-Ch-Ua-Full-Version-List": 'Chromium";v="116.0.5845.97", "Not)A;Brand";v="24.0.0.0", "Google Chrome";v="116.0.5845.97"',
            "Sec-Ch-Ua-Mobile": '?0',
            "Sec-Ch-Ua-Model": "",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Ch-Ua-Platform-Version": '15.0.0"',
            "Sec-Fetch-Dest": 'document',
            "Sec-Fetch-Mode": 'navigate',
            "Sec-Fetch-Site": 'same-origin',
            "Sec-Fetch-User": '?1',
            "Upgrade-Insecure-Requests": '1',
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            "Viewport-Width": '1920'
        }

    def saveResponseToFile(self, response_content):
        with open("facebook_page.html", "w", encoding="utf-8") as file:
            file.write(response_content)

    def getHomeFacebook(self):
        response = requests.get("https://www.facebook.com/", headers=self.header)
        if response.status_code == 200:
            self.saveResponseToFile(response.text)
            print("Đã ghi nội dung vào file facebook_page.html")
        else:
            print("Yêu cầu không thành công")


if __name__ == "__main__":
    ApiFacebook().getHomeFacebook()
