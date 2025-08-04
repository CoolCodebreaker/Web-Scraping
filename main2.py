from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--start-maximized")


driver = webdriver.Chrome(options=options)


driver.get("https://www.google.com")

try:
   consent_button = driver.find_element(By.XPATH, "//button/div[normalize-space()='Reject all']")
   consent_button.click()
except:
    pass

time.sleep(5)

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("P")
time.sleep(0.5)
search_box.send_keys("h")
time.sleep(1)
search_box.send_keys("y")
time.sleep(0.7)
search_box.send_keys("s")
time.sleep(1.2)
search_box.send_keys("i")
time.sleep(0.5)
search_box.send_keys("c")
time.sleep(1)
search_box.send_keys("s")
search_box.send_keys(Keys.RETURN)


time.sleep(2)

try:
    results = driver.find_elements(By.XPATH, "//*[@id='b_results']/li[2]/div[3]/h2/a")
    print("Trying 0000")
    for result in results:
        href = result.get_attribute("href")
        if "bing" not in href:
            result.click()
            break
except Exception as e:
    print("Error clicking result:", e)


time.sleep(5)
driver.quit()