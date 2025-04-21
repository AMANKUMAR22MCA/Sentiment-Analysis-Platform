from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrape_flipkart_reviews(product_url, product_name):
    driver = webdriver.Chrome()
    driver.get(product_url)
    time.sleep(3)

    reviews = []

    for page in range(3):  # Loop through 5 pages
        # print(f"\n🟡 Scraping page {page + 1}...")
        
        review_boxes = driver.find_elements(By.CLASS_NAME, "col.EPCmJX")
        print(f"🔍 Found {len(review_boxes)} review boxes")

        for idx, box in enumerate(review_boxes):
            try:
                rating_el = box.find_element(By.CLASS_NAME, "XQDdHH.Ga3i8K")
                rating = int(rating_el.text.strip()) if rating_el.text.strip().isdigit() else "N/A"

                review_el = box.find_element(By.CLASS_NAME, "z9E0IG")
                review = review_el.text.strip()

                # print(f"✅ Review {idx + 1}: {rating} stars - {review[:50]}...")

                reviews.append({
                    "product": product_name,
                    "rating": rating,
                    "review": review
                })
            except Exception as e:
                print(f"❌ Error reading review {idx + 1}: {e}")
                continue

        try:
            next_button = driver.find_element(By.CLASS_NAME, "WSL9JP")
            print("➡️ Clicking next page...")
            next_button.click()
            time.sleep(3)
        except Exception as e:
            print(f"⛔ Next button error: {e}")
            break

    driver.quit()
    # print(f"\n🎯 Total reviews scraped: {len(reviews)}")
    return reviews


