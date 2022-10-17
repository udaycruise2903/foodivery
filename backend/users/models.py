from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField(blank=False)
    street_line1 = models.CharField(('Address 1'), max_length = 100, null=False, blank = True)
    street_line2 = models.CharField(('Address 2'), max_length = 100, blank = True)
    zipcode = models.CharField(('ZIP Code'), max_length = 6, null=False, blank=True)
    city = models.CharField(('City'), max_length = 100, blank=True)
    state = models.CharField(('State'), max_length = 50, blank=True)

    def __str__(self):
        return self.user_name


