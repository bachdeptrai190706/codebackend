from django.db import models
from django.contrib.auth.models import User
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    number = models.DecimalField(max_digits=10, decimal_places=0)
    def __str__(self):
        return self.name
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.product.price * self.quantity
class Order(models.Model):
    PAYMENT_CHOICES = [
        ('cash', 'Thanh toán khi nhận hàng'),
        ('card', 'Thẻ ngân hàng'),
        ('momo', 'Momo/ZaloPay')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.cart.items.all())
  