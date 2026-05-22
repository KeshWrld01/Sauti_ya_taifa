from django.db import models

class SolidarityMessage(models.Model):
    sender_name = models.CharField(max_length=100, blank=True, default='Anonymous')
    message = models.TextField()
    county = models.CharField(max_length=50, blank=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender_name} — {self.message[:50]}"

class FamilyDonation(models.Model):
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    checkout_request_id = models.CharField(max_length=100, blank=True)
    mpesa_receipt_number = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone_number} — KES {self.amount} — {self.status}"