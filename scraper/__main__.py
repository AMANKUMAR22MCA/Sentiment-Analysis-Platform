from login import get_access_token
from scraper import scrape_flipkart_reviews
from push_reviews import push_reviews_to_api

if __name__ == "__main__":
    email = "rahul@gmail.com"     # 👈 replace with real user
    password = "123456"   # 👈 replace with real password

    token = get_access_token(email, password)

    products = [
        {
            "name": "Redmi Note 13",
            "url": "https://www.flipkart.com/redmi-note-13-5g-chromatic-purple-256-gb/product-reviews/itmf0a3e4e21fcc3?pid=MOBHFM37FTDRENMH&lid=LSTMOBHFM37FTDRENMHD2T1LD&marketplace=FLIPKART"
        },
        {
            "name":"IQOO z9x",
            "url":"https://www.flipkart.com/iqoo-z9x-tornado-green-128-gb/product-reviews/itm37ed9034fd805?pid=MOBHF76GH8XPQB3X&lid=LSTMOBHF76GH8XPQB3XOZNTCF&marketplace=FLIPKART"
        }

        # Add more products
    ]

    all_reviews = []
    for product in products:
        reviews = scrape_flipkart_reviews(product["url"], product["name"])
        all_reviews.extend(reviews)

    push_reviews_to_api(all_reviews, token)


# if __name__ == "__main__":
#     reviews = scrape_flipkart_reviews(
#         "https://www.flipkart.com/redmi-note-13-5g-chromatic-purple-256-gb/product-reviews/itmf0a3e4e21fcc3?pid=MOBHFM37FTDRENMH&lid=LSTMOBHFM37FTDRENMHD2T1LD&marketplace=FLIPKART",
#         "Redmi Note 13"
#     )

#     for i, review in enumerate(reviews):
#         print(f"{i+1}. Rating: {review['rating']} | Review: {review['review'][:100]}...")
    
#     print(f"\nTotal reviews scraped: {len(reviews)}")
