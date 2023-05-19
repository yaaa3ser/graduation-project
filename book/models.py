from django.db import models

class Cart(models.Model):
    books = models.ManyToManyField('Book', related_name='carts')

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title + str(self.id)
