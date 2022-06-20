from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options 

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(ChromeDriverManager().install())

#For Mac - If you use windows change the chromedriver location
chrome_path = '/usr/lib/chromium-browser/chromedriver'
driver = webdriver.Chrome(chrome_path)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-popup-blocking")

driver.maximize_window()
driver.get("https://adviserinfo.sec.gov/compilation")

# driver.get("https://adviserinfo.sec.gov/")
# tabName = driver.find_element_by_link_text("Investment Adviser Data")
# tabName.click()

time.sleep(3)

# report1 = driver.find_element_by_xpath("//div[@class='compilation-container ng-scope layout-column flex']//div[1]//div[1]//div[1]//div[2]//button[1]")

report1 = driver.find_element_by_xpath("//button[@analytics-label='IAPD - SEC Investment Adviser Report (GZIP)']")

# print(report1)
report1.click()

time.sleep(5)

driver.close()