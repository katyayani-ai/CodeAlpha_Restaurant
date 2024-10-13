# restaurant/models.py
from django.db import models

# Menu Model
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available_quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name

# Order Model
class Order(models.Model):
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        # Calculate total price
        self.total_price = self.item.price * self.quantity
        super(Order, self).save(*args, **kwargs)

# Reservation Model
class Reservation(models.Model):
    customer_name = models.CharField(max_length=100)
    reservation_date = models.DateTimeField()
    table_number = models.IntegerField()

    def __str__(self):
        return f"{self.customer_name} - Table {self.table_number}"
