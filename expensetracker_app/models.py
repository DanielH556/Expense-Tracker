from django.db import models

"""## Expense Input
 - Product Name (varchar)
 - Price (float)
 - Store (varchar)
 - Date (date)
 - Type of product (varchar)
"""
class Expense(models.Model):
   productName = models.CharField(max_length=200)
   price = models.FloatField(default=0)
   store = models.CharField(max_length=100)
   purchaseDate = models.DateTimeField("date published")
   productType = models.CharField(max_length=100)
