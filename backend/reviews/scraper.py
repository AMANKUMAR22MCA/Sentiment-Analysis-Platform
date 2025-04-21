# review/scraper.py

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrape_flipkart_reviews(product_url, product_name):
    driver = webdriver.Chrome()
    driver.get(product_url)
    time.sleep(2)

    reviews = []
    for _ in range(2):  # adjust this for more pages
        review_boxes = driver.find_elements(By.CLASS_NAME, "col.EPCmJX")
        for box in review_boxes:
            try:
                rating = int(box.find_element(By.CLASS_NAME, "XQDdHH.Ga3i8K").text.strip())
                review = box.find_element(By.CLASS_NAME, "z9E0IG").text.strip()
                reviews.append({
                    "product": product_name,
                    "rating": rating,
                    "review": review
                })
            except:
                continue

        try:
            next_button = driver.find_element(By.CLASS_NAME, "WSL9JP")
            next_button.click()
            time.sleep(2)
        except:
            break

    driver.quit()
    return reviews
