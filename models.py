from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='No description available')  # Set a default value
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order of {self.quantity} {self.menu_item.name}"

class Reservation(models.Model):
    customer_name = models.CharField(max_length=100)
    reservation_date = models.DateTimeField()
    table_number = models.PositiveIntegerField()

    def __str__(self):
        return f"Reservation for {self.customer_name} at table {self.table_number}"
