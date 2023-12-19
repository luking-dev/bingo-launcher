import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from urllib3.exceptions import NewConnectionError, MaxRetryError

def element_checked(element):
    return element.get_attribute('class')

def check_element(element, invert=True):
    if invert or 'checked' not in element.get_attribute('class'):
        element.click()

options = ChromeOptions()
arguments = [
    '--start-maximized',
    '--enable-javascript',
    '--no-sandbox',
    '--kiosk',
    '--disable-gpu',
]
for argument in arguments:
    options.add_argument(argument)

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

service = Service()
driver = Chrome(service=service, options=options)
print('> Running browser...\n')
    
try:    
    url = 'https://90ball.letsplaybingo.io/'
    driver.get(url)

    wait = Wait(driver, 5)

    wild_bingo = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/section[2]/div/div[2]/section/div[1]/div[2]/div[2]/div[1]/label')))

    autoplay_speed = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/section[2]/div/div[2]/section/div[2]/div[1]/div[2]/div/div[2]/div/div[4]')))
    
    # Slider
    driver.execute_script('document.getElementsByClassName("rc-slider-track")[0].style = "width: 100%"')
    driver.execute_script('document.getElementsByClassName("rc-slider-handle")[0].style = "right: 100%"')

    audible_caller = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/section[2]/div/div[2]/section/div[2]/div[2]/div[2]/div[1]/div[1]/label')))
    check_element(audible_caller)

    double_call = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/section[2]/div/div[2]/section/div[2]/div[2]/div[2]/div[1]/div[2]/label')))
    check_element(double_call)

    chatty = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/section[2]/div/div[2]/section/div[2]/div[2]/div[2]/div[1]/div[3]/label')))
    if element_checked(chatty):
        check_element(chatty)
        
    caller_selection = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/section[2]/div/div[2]/section/div[2]/div[3]/div[2]/div/div/div[1]/div[1]')))
    caller_selection.click()
    ActionChains(driver).send_keys('Microsoft Helena').perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    
    audible_chime = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/section[2]/div/div[2]/section/div[2]/div[4]/div[2]/label')))
    check_element(audible_chime)
    
    chime_selection = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/section[2]/div/div[2]/section/div[2]/div[5]/div[2]/div/div')))
    chime_selection.click()
    ActionChains(driver).send_keys('Chime 2').perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()

    start_autoplay = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/section[2]/div/div[1]/section/div/button[2]')))
    time.sleep(30)
    start_autoplay.click()
    
    input('> Press any key to finish...\n')

except (KeyboardInterrupt, ConnectionRefusedError, MaxRetryError, NewConnectionError):
    driver.close()
    driver.quit()
