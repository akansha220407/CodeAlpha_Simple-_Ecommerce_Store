from django.test import TestCase
from django.contrib.auth.models import User
from .models import Product, Order, OrderItem

class ProductModelTest(TestCase):
    def test_product_creation(self):
        product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=9.99
        )
        self.assertEqual(str(product), "Test Product")

class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.product = Product.objects.create(name="Test Product", price=9.99)

    def test_order_creation(self):
        order = Order.objects.create(user=self.user)
        self.assertEqual(str(order), f"Order {order.id} by testuser")
