from django.db import models
import uuid
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    verification_code = models.CharField(max_length=6, null=True, blank=True)
    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+?\d{10,14}$', message="Phone number must be 10 to 14 digits, optionally starting with +.")],
        blank=True
    )
    email = models.EmailField(unique=True)  # Set the email field as unique
    email_verified = models.BooleanField(default=False)  # New field to track email verification status
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    # Status of the user - 'verified' or 'unverified'
    STATUS_CHOICES = [
        ('verified', 'Verified'),
        ('unverified', 'Unverified'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='unverified')  # New field to track the status

    # Status of the account - 'enabled' or 'disabled'
    ACCOUNT_STATUS_CHOICES = [
        ('enabled', 'Enabled'),
        ('disabled', 'Disabled'),
    ]
    account_status = models.CharField(max_length=10, choices=ACCOUNT_STATUS_CHOICES, default='disabled')  # New field to track the account status


class Company(models.Model):
    uid = models.CharField(max_length=20, unique=True)  # Unique Identifier
    name = models.CharField(max_length=255)
    legal_form = models.CharField(max_length=100)
    registration_date = models.DateField()
    legal_status = models.CharField(max_length=50, choices=[('Active', 'Active'), ('Dissolved', 'Dissolved')])
    headquarters = models.CharField(max_length=255)
    sector = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=100)
    company = models.ForeignKey(Company, related_name='directors', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class HistoricalChange(models.Model):
    company = models.ForeignKey(Company, related_name='history', on_delete=models.CASCADE)
    change_type = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.change_type} on {self.date}"

