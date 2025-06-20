from django.db import models
from django.contrib.auth.models import User

from shop.models import Product


class FavoriteProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favorited_by')
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s favorite product: {self.product.name}"

    class Meta:
        unique_together = ('user', 'product')
        verbose_name = 'Favorite Product'
        verbose_name_plural = 'Favorite Products'
        ordering = ('-added_at', )

