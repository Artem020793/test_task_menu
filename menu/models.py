from django.db import models
from django.utils import timezone


class Menu(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title


class Dish(models.Model):
    name = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()
    price = models.FloatField()
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
