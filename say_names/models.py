from django.db import models

class Victim(models.Model):
    STATUS_CHOICES = [
        ('killed', 'Killed'),
        ('jailed', 'Jailed'),
        ('injured', 'Injured'),
        ('missing', 'Missing'),
    ]

    APPROVAL_CHOICES = [
        ('pending', 'Pending Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    county = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    date_of_incident = models.DateField(null=True, blank=True)
    how_it_happened = models.TextField()
    additional_info = models.TextField(blank=True)
    photo = models.ImageField(upload_to='victims/', blank=True, null=True)
    approval = models.CharField(max_length=20, choices=APPROVAL_CHOICES, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} — {self.status} — {self.approval}"