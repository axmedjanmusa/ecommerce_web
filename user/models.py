from django.contrib.auth import get_user_model
from django.db import models

from shop.models import Product

User = get_user_model()

class Profile(models.Model):
    photo = models.ImageField(upload_to='profiles/', null=True, blank=True)
    phone = models.CharField(max_length=255, default="")
    country = models.CharField(max_length=255, default="")
    city = models.CharField(max_length=255, default="")
    job = models.CharField(max_length=255, default="")
    bio = models.TextField(max_length=255, null=True, blank=True)

    user = models.OneToOneField(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

class Comment(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Id: {self.id} | Author: {self.author.username}"

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"