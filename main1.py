from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time


driver = webdriver.Chrome()


driver.get("https://www.bing.com")

time.sleep(2)

try:
    consent_button = driver.find_element(By.CSS_SELECTOR, "#bnp_btn_reject")
    consent_button.click()
except:
    pass

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Physics")
search_box.send_keys(Keys.RETURN)


time.sleep(2)

try:
    results = driver.find_elements(By.CSS_SELECTOR, "#b_results > li.b_algo.b_algoBorder.b_algoBigWiki.b_algo_feedback.b_algoBigWiki2.b_wiki_bg_color_kc > div.b_algo_group > h2 > a")
    print(results)
    try:
        q_button = driver.find_element(By.CSS_SELECTOR, "#b_vfly_64673 > div > div")
        q_button.click()
    except:
        pass
    try:
        consent_button = driver.find_element(By.CSS_SELECTOR, "#bnp_btn_reject")
        consent_button.click()
    except:
        pass
    try:
        for result in results:
            href = result.get_attribute("href")
            if "bing" not in href:
                result.click()
                break
    except:
        pass
except Exception as e:
    print("ERROR...", e)

time.sleep(300)
driver.quit()