from django.db import models
import datetime

# Categories of classes
class Category (models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Customer(models.Model):
    first_name =  models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    user_name = models.CharField(max_length=50)

    def __str__(self):
        return F'{self.first_name} {self.last_name}'
      

class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default="", blank=True, null=True )

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date =  models.DateField(default=datetime.datetime.today)
    #staus = models.BooleanField(default=False)

    def __str__(self):
        return self.product
