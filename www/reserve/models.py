from django.conf import settings
from django.db import models


# Create your models here.
class FieldType(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Field(models.Model):
    name = models.CharField(max_length=45)
    field_type = models.ForeignKey(FieldType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Price(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    reservation_time = models.IntegerField()
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.field} - {self.price}'


class Block(models.Model):
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f'{self.start_time} - {self.end_time}'


class Reserve(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    day = models.DateField()
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    reserve_price = models.ForeignKey(Price, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.day}'

