# CÁCH NÀY DÙNG THỂ LOẠI AUTOCLICK
# NẾU LỖI Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)')))
# hãy thực thi: pip install pip-system-certs (hoặc thêm verify=False ở dòng 39 bên dưới)

# xem mô phỏng ở đây: https://youtu.be/Dfj3N5SXxXo
import time
import requests
from undetected_chromedriver import Chrome
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# thay đỏi để phù hợp vs bạn
EMAIL="22110999@student.hcmute.edu.vn"
PASSWORD="123456789"
class TuoiThoDaKhoc:
    def __init__(self) -> None:
        self.url = 'https://accounts.google.com/signin/v2/challenge/dp?gsiwebsdk=3&client_id=216817404167-enbal04c37hsv19pofeebine18hm126f.apps.googleusercontent.com&scope=openid+profile+email&redirect_uri=storagerelay%3A%2F%2Fhttps%2Fdkmh.hcmute.edu.vn%3Fid%3Dauth511451&prompt=select_account&response_type=token&include_granted_scopes=true&enable_granular_consent=true&service=lso&o2v=2&theme=glif&flowName=GeneralOAuthFlow&cid=3&navigationDirection=forward&TL='
        self.driver = Chrome(use_subprocess=True)
        self.driver.get(self.url)
        self.time = 10
    def login(self):
        sleep(0.5)
        self.driver.find_element(By.ID, 'identifierId').click()
        self.driver.find_element(By.ID, 'identifierId').send_keys(EMAIL)
        self.driver.find_element(By.ID, 'identifierNext').click()
        time.sleep(6)
        self.driver.find_element(By.CLASS_NAME, 'Xb9hP').click()
        self.driver.find_element(By.NAME, 'Passwd').send_keys(PASSWORD)
        self.driver.find_element(By.CLASS_NAME, 'Jskylb ').click()
        sleep(4)
        self.code()
    def code(self):
        content = self.driver.page_source
        t=content[content.index('ya29'):content.index(
            '\&quot;', content.index('ya29')+11)]
        try:
            tk=requests.post("https://dangkyapi.hcmute.edu.vn/api/Authen/AuthenticateGoogle?apiKey=pscRBF0zT2Mqo6vMw69YMOH43IrB2RtXBS0EHit2kzv&clientId=dtl",json={
            'Token':t
            })
            tuoitho=tk.json()
            print(tuoitho['Token'])
            # sau khi có đc cái này thì bạn biết sẽ dùng nó để làm những j rồi!
        except:
            print('error')
if __name__ == "__main__":
    ttdk = TuoiThoDaKhoc()
    ttdk.login()
