# 🧠 Sentiment Analysis Platform

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.x-green.svg)](https://www.djangoproject.com/)
[![Selenium](https://img.shields.io/badge/Selenium-Automation-yellow.svg)](https://www.selenium.dev/)
[![Transformers](https://img.shields.io/badge/Transformers-HuggingFace-red.svg)](https://huggingface.co/)
[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](https://opensource.org/licenses/MIT)

> A full-stack platform to **scrape reviews from Flipkart**, **analyze sentiments using HuggingFace Transformers**, and provide **pros & cons summaries** — all via a Django backend secured with JWT and automated with Selenium.

---

## 🚀 Features

- 🔐 **JWT Authentication** – Register and login using token-based security
- 📝 **Review CRUD** – Create, update, and delete reviews from the UI or API
- 🤖 **Sentiment Analysis** – Summarize likes and dislikes from product reviews using Hugging Face models
- ⚙️ **Flipkart Scraper** – Extract live product reviews using Selenium automation
- 🧰 **CLI Tool** – Command-line interface for selecting a product and analyzing its sentiment
- 📊 **Dashboard** – Optional frontend to view review stats and control scraping

---

## 🛠️ Tech Stack

| Layer        | Tools Used                                  |
|--------------|----------------------------------------------|
| Backend API  | Django REST Framework, JWT, MySQL            |
| Scraper      | Selenium, BeautifulSoup                      |
| LLMs         | HuggingFace Transformers, PyTorch            |
| Auth         | Simple JWT                                   |
| Frontend     | HTML, CSS (optional dashboard)               |
| CLI          | Python CLI (`argparse`, `requests`)          |

---

## 🔗 API Endpoints

| Endpoint                        | Method | Description                                 | Auth Required |
|---------------------------------|--------|---------------------------------------------|---------------|
| `/api/register/`               | POST   | Register a new user                         | ❌ No         |
| `/api/login/`                  | POST   | Obtain JWT tokens                           | ❌ No         |
| `/api/reviews/`                | GET    | List all reviews                            | ✅ Yes        |
| `/api/reviews/`                | POST   | Create a new review                         | ✅ Yes        |
| `/api/reviews/{id}/`           | PUT    | Update a review                             | ✅ Yes        |
| `/api/reviews/{id}/`           | DELETE | Delete a review                             | ✅ Yes        |
| `/api/reviews/?product=name`   | GET    | Fetch reviews for a specific product        | ✅ Yes        |
| `/api/reviews/product/`        | GET    | Get list of unique product names            | ✅ Yes        |

---

## 📸 Screenshots

| Register Page | Dashboard |
|---------------|-----------|
| ![login](https://github.com/user-attachments/assets/026dffef-4422-4231-80c3-e1e277cb9c6a) | ![dashboard](https://github.com/user-attachments/assets/157c977c-1bcb-4dfe-8583-364713ebbad6) |
| ![register](![image](https://github.com/user-attachments/assets/3bc011f3-c460-4bce-8d13-c0abb2221af3)
) |
> 🔒 Only **authenticated users** can scrape reviews using the dashboard.  
> 🛒 Scraped reviews from Flipkart are stored directly in the database using the logged-in user's JWT token.

![image](https://github.com/user-attachments/assets/6391e21d-20c6-4da2-b0c5-f8a9f853407e) <br>
![image](https://github.com/user-attachments/assets/02c9cb8c-408e-41f8-aabd-2a42cb23cc57)


---

## 🧪 How to Use

### 🔧 Setup Instructions

```
# Clone the repository
git clone https://github.com/AMANKUMAR22MCA/Sentiment-Analysis-Platform.git
cd Sentiment-Analysis-Platform

# Create and activate virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py makemigrations users
python manage.py makemigrations reviews
python manage.py migrate

# Run the server
python manage.py runserver

```


## ⚙️ CLI Usage 
# Run CLI script for scraping and sentiment summary
python sentiment_cli.py

