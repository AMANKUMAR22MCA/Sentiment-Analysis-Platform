import os
import openai
from dotenv import load_dotenv
import requests
from urllib.parse import quote  # Import quote for URL encoding

# Load environment variables from .env
load_dotenv()

# Get OpenAI API key from .env
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to get product reviews from the API
def get_reviews_for_product(product_name):
    # Encode the product name to handle spaces and special characters
    encoded_product_name = quote(product_name)
    print(encoded_product_name)
    # Make the API call with the encoded product name
    response = requests.get(f'http://localhost:8000/api/reviews/?product={encoded_product_name}')
    print(response)
    if response.status_code == 200:
        return response.json()
    else:
        return []

# Function to analyze sentiment
def analyze_sentiment(reviews):
    # Example: Analyze sentiment using OpenAI GPT-3
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user", 
            "content": f"Analyze the following reviews for product sentiment: {reviews}"
        }]
    )
    return response["choices"][0]["message"]["content"]

# Main CLI functionality
def main():
    product_name = input("Enter product name: ")

    # Get reviews for the selected product
    reviews = get_reviews_for_product(product_name)

    if reviews:
        review_texts = " ".join([review['review'] for review in reviews])
        sentiment = analyze_sentiment(review_texts)
        print(f"Sentiment Analysis for {product_name}:")
        print(sentiment)
    else:
        print(f"No reviews found for {product_name}")

if __name__ == "__main__":
    main()
