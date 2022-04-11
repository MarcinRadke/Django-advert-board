from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    ordering = models.IntegerField()

class Offer(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)