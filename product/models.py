from django.db import models


# Create your models here.
class Category(models.Model):
    class Meta:
        db_table = 'category'

    name = models.CharField(max_length=256)


class Drink(models.Model):
    class Meta:
        db_table = "drink"

    title = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
