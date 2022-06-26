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
    driver.get('http://dig.ccmixter.org/search?limit=3715&searchp=instrumental')
    html = driver.page_source
    time.sleep(10)
    print(html)
    #use the id number before the song name to get the xpath of the button that is to be clicked
    #<button class="btn btn-warning  btn-lg" data-reactid=".0.1.6.0.2.0.0.1.$8460.2.0"><i class="fa fa-cloud-download" data-reactid=".0.1.6.0.2.0.0.1.$8460.2.0.0"></i></button>
    #button_element = driver.find_element_by_xpath("//button[@class='btn btn-warning  btn-lg' and @data-reactid='.0.1.6.0.2.0.0.1.$"+random_song[0]+".2.0']")
    button_element = driver.find_element_by_xpath("//button[@class='btn btn-warning  btn-lg' and @data-reactid='.0.1.6.0.2.0.0.1.$8460.2.0']")
    #button_element = driver.find_element_by_xpath("//button[@class='btn btn-warning  btn-lg' and @data-reactid='.0.1.6.0.2.0.0.1.$64427.2.0']")
    WebDriverWait(driver,10).until(EC.element_to_be_clickable(button_element)).click()
    driver.switch_to.active_element
    time.sleep(4)
    html = driver.page_source
    
    time.sleep(4)
    #print('ffffff', html)

    mp3_url = 'http://ccmixter.org/' + str(html).split('.mp3" download=""')[0].split('http://ccmixter.org/')[1] + '.mp3'
    print(mp3_url)

main()