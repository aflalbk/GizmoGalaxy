from django.db import models

# Create your models here.
class Product(models.Model):
    live = 1
    delete = 0
    delete_choices = ((live,'live'),(delete,'delete'))

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    rating = models.FloatField()
    image = models.ImageField(upload_to="media/product_image/", blank=True, null=True)
    stock = models.IntegerField(blank=True,null=True)
    warranty = models.IntegerField(blank=True,null=True)
    priority = models.IntegerField(default=0)
    delete_status = models.IntegerField(choices=delete_choices, default=live)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

