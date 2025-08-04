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
    results = driver.find_elements(By.CSS_SELECTOR, "#b_results > li.b_algo.b_algoBorder.b_algoBigWiki.b_algo_feedback.b_algoBigWiki2.b_wiki_bg_color_kc > div.b_algo_group > h2 > a")
    print("ABCDEFGHHIJKLMNOP"+str(results))
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

time.sleep(5)

#with open ('test1.csv', 'w') as fi:
    #for i in results:
       # print(i.text)
        #fi.write(i.text)

try:
    time.sleep(5)
    title = driver.find_element(By.ID, "firstHeading").text #'no such element' error for some reason
    print("TITLE: "+ title)
    content = driver.find_element(By.XPATH, "//*[@id='mw-content-text']/div[1]/p[2]") #'no such element' error for some reason
    print("CONTENT: "+ content.text)
    with open ('test1.csv', 'w') as fi: #this should work once the NoSuchElementError above is fixed
        fi.write(title.text)
        fi.write(content.text)
except Exception as e:
    print("ERROR...", e)

#with open ('test1.csv', 'w') as fi: #this should work once the NoSuchElementError above is fixed
        #fi.write(title.text)
        #fi.write(content.text)

time.sleep(3)
driver.quit()