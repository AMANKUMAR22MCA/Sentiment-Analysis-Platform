from rest_framework import generics, permissions
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from rest_framework.views import APIView
class AddReviewView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

class UniqueProductsView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Review.objects.all()
        product = self.request.query_params.get('product')
        if product:
            queryset = queryset.filter(product__icontains=product)
        return queryset


class ReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Review.objects.all()
        product = self.request.query_params.get('product')
        if product:
            queryset = queryset.filter(product__icontains=product)
        return queryset


class ReviewUpdateView(generics.UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class ReviewDeleteView(generics.DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]


# class UniqueProductsView(APIView):
#     # permission_classes = [IsAuthenticated]

#     def get(self, request, *args, **kwargs):
#         products = Review.objects.values_list("product", flat=True).distinct()
#         return Response(list(products))
# review/views.py

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .scraper import scrape_flipkart_reviews
from .push_reviews import push_reviews_to_api  # if you have this

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def trigger_scraping(request):
    user = request.user
    token = request.auth  # JWT access token from frontend
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

    return Response({"message": "Scraping completed", "count": len(all_reviews)})
