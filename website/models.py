from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be in the format: '+999999999'. Up to 12 digits allowed."
    )
    phone = models.CharField(validators=[phone_regex],max_length=12)
    message = models.CharField(max_length=500)

    def __str__(self):
        return f'Message from {self.name}'