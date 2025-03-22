from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Customer(AbstractUser):
    live=1
    delete=0
    delete_choices = ((live,'live'),(delete,'delete'))

    address = models.TextField()
    phone = models.CharField(max_length=10)
    profile_picture = models.ImageField(upload_to='media/profile_pics/', blank=True, null=True)
    is_seller = models.BooleanField(default=False)
    delete_status = models.IntegerField(choices=delete_choices,default=live)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.username