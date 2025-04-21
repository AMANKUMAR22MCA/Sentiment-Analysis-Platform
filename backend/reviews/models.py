from django.db import models
from users.models import User

class Review(models.Model):
    product = models.CharField(max_length=255)
    rating = models.IntegerField()
    review = models.TextField()

    created_by = models.ForeignKey(User, related_name='created_reviews', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='updated_reviews', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product} - {self.rating} ⭐"
