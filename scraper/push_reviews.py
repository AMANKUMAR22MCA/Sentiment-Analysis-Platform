import requests

def push_reviews_to_api(reviews, token):
    url = "http://localhost:8000/api/reviews/add/"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    for review in reviews:
        response = requests.post(url, json=review, headers=headers)
        print(f"{review['product']} - {response.status_code} - {response.text}")
