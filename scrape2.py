from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def main():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('http://dig.ccmixter.org/search?limit=10&searchp=instrumental')
    html = driver.page_source
    time.sleep(2)
    print(html)

    print('tj')

    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"li.clearfix:nth-child(1) > span:nth-child(3) > button:nth-child(1)"))).click()
    
    
    
    html = driver.page_source
    time.sleep(10)
    print(html)

main()