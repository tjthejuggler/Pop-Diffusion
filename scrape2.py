from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def main():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("window-size=1400,600")
    driver = webdriver.Chrome(chrome_options=options, executable_path=ChromeDriverManager().install())
    driver.get('http://dig.ccmixter.org/search?limit=10&searchp=instrumental')
    html = driver.page_source
    time.sleep(2)
    print(html)
    #use the id number before the song name to get the xpath of the button that is to be clicked
    button_element = driver.find_element_by_xpath("//button[@class='btn btn-warning  btn-lg' and @data-reactid='.0.1.6.0.2.0.0.1.$64427.2.0']")
    WebDriverWait(driver,10).until(EC.element_to_be_clickable(button_element)).click()
    driver.switch_to.active_element
    time.sleep(4)
    html = driver.page_source
    download_button = driver.find_element_by_xpath("//button[@class='btn btn-info btn-lg' and @data-reactid='.0.1.6.0.2.0.0.1.$64427.2.1.0.0.1.1.1.0.0.0']")
    WebDriverWait(driver,10).until(EC.element_to_be_clickable(button_element)).click()
    #<a class="btn btn-info btn-lg" href="http://ccmixter.org/content/airtone/airtone_-_bluenotes_6.mp3" download="" data-reactid=".0.1.6.0.2.0.0.1.$64427.2.1.0.0.1.1.1.0.0.0"><i class="fa fa-cloud-download fa-2x pull-left" data-reactid=".0.1.6.0.2.0.0.1.$64427.2.1.0.0.1.1.1.0.0.0.0"></i><span data-reactid=".0.1.6.0.2.0.0.1.$64427.2.1.0.0.1.1.1.0.0.0.1"> Download </span><small data-reactid=".0.1.6.0.2.0.0.1.$64427.2.1.0.0.1.1.1.0.0.0.2">8.73MB</small></a>
    time.sleep(4)
    print(html)

main()