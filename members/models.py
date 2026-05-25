from django.db import models
import uuid

class Member(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending Payment'),
        ('active', 'Active'),
        ('expired', 'Expired'),
    ]

    member_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    id_number = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=15)
    county = models.CharField(max_length=50)
    registration_fee = models.DecimalField(max_digits=10, decimal_places=2, default=500)
    subscription_fee = models.DecimalField(max_digits=10, decimal_places=2, default=500)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=1000)
    checkout_request_id = models.CharField(max_length=100, blank=True)
    mpesa_receipt_number = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    joined_at = models.DateTimeField(auto_now_add=True)
    subscription_expires = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.full_name} — {self.status}"