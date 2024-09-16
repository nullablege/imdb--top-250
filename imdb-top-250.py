from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from urllib.parse import urlparse, parse_qs


options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
prefs = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("prefs", prefs)
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-blink-features=AutomationControlled")


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)

driver.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
element = WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#__next > main > div > div.ipc-page-content-container.ipc-page-content-container--center > section > div > div.ipc-page-grid.ipc-page-grid--bias-left > div > ul > li:nth-child(250) > div.ipc-metadata-list-summary-item__c > div > div > div.ipc-title.ipc-title--base.ipc-title--title.ipc-title-link-no-icon.ipc-title--on-textPrimary.sc-b189961a-9.bnSrml.cli-title > a"))  
    )
liler = driver.find_elements(By.CLASS_NAME,"TwzGn")
for li in liler:
    baslik = li.find_element(By.CLASS_NAME,"ipc-title__text").text
    veriler = li.find_elements(By.CSS_SELECTOR,".sc-b189961a-7 > span")
    puan = driver.find_element(By.CLASS_NAME,"ipc-rating-star--rating").text
    try:
        print(f"{veriler[0].text} Published in {baslik} {veriler[1].text} Movie in length {veriler[2].text} and its score {puan} ")
    except:
        pass
    
