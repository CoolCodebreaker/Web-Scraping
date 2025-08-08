from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.bing.com")

    # Dismiss Bing consent popup
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "bnp_btn_reject"))).click()
    except:
        pass

    # Search for "Physics"
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Physics Wikipedia")
    search_box.send_keys(Keys.RETURN)

    time.sleep(2)

    # Find first Wikipedia link
    wiki_link = None
    links = driver.find_elements(By.CSS_SELECTOR, "li.b_algo h2 a")
    for link in links:
        href = link.get_attribute("href")
        if "wikipedia.org" in href:
            wiki_link = href
            break

    if not wiki_link:
        print("No Wikipedia link found.")
        driver.quit()
        exit()

    driver.get(wiki_link)

    # Wait for Wikipedia page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "firstHeading"))
    )

    # Get title and first paragraph
    title = driver.find_element(By.ID, "firstHeading").text

    try:
        paragraph = driver.find_element(By.CSS_SELECTOR, "#mw-content-text p").text
    except:
        paragraph = "First paragraph not found"

    print("TITLE:", title)
    print("PARAGRAPH:", paragraph)

    # Save to CSV
    with open('test1.csv', 'w') as f:
        f.write(f'"{title}","{paragraph}"\n')

finally:
    time.sleep(2)
    driver.quit()
