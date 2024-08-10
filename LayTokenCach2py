import requests
from undetected_chromedriver import Chrome
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


cookie_str='cookie dạng string'
cookie_dict=dict(item.split('=',1) for item in cookie_str.split('; '))
cookie_list=[]
for key, value in cookie_dict.items():
    cookie_list.append({"name": key, "value": value})

class Google:
    def __init__(self) -> None:
        self.url = 'https://accounts.google.com/signin/v2/challenge/dp?gsiwebsdk=3&client_id=216817404167-enbal04c37hsv19pofeebine18hm126f.apps.googleusercontent.com&scope=openid+profile+email&redirect_uri=storagerelay%3A%2F%2Fhttps%2Fdkmh.hcmute.edu.vn%3Fid%3Dauth511451&prompt=select_account&response_type=token&include_granted_scopes=true&enable_granular_consent=true&service=lso&o2v=2&theme=glif&flowName=GeneralOAuthFlow&cid=3&navigationDirection=forward&TL='
        self.driver = Chrome(use_subprocess=True,headless=False)
        self.driver.get(self.url)
        for cookie in cookie_list:
            self.driver.add_cookie(cookie)
    def login(self):
        # pass
        self.driver.get(self.url)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'LbOduc'))).click()
        sleep(3)
        self.code()

    def code(self):
        # pass
        content = self.driver.page_source
        t=content[content.index('ya29'):content.index(
            '\&quot;', content.index('ya29')+11)]
        print(t)
        # print(content)
        self.driver.close()
        tk=requests.post("https://dangkyapi.hcmute.edu.vn/api/Authen/AuthenticateGoogle?apiKey=pscRBF0zT2Mqo6vMw69YMOH43IrB2RtXBS0EHit2kzv&clientId=dtl",json={
          'Token':t
        })
        print(tk.json())
        

if __name__ == "__main__":
    google = Google()
    google.login()
    
    
