from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )
    quantity = models.PositiveIntegerField(default=0)
    is_discounted = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    wishlisted_by = models.ManyToManyField(User,blank=True,related_name='wishlist')

    def main_image(self):
        first = self.images.first()
        if first:
            return first.image.url
        return None

    def __str__(self):
        return self.name


    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image for {self.product.name}"