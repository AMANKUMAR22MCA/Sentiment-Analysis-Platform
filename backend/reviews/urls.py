from django.urls import path
from .views import AddReviewView, ReviewListView, ReviewUpdateView, ReviewDeleteView,trigger_scraping,UniqueProductsView

urlpatterns = [
    path('add/', AddReviewView.as_view(), name='add-review'),
    path('search/', ReviewListView.as_view(), name='search-reviews'),
    path('update/<int:pk>/', ReviewUpdateView.as_view(), name='update-review'),
    path('delete/<int:pk>/', ReviewDeleteView.as_view(), name='delete-review'),
    path("scrape/", trigger_scraping),
    path("", UniqueProductsView.as_view(), name="unique-products"),
]


