from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, null=True,blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="user3.jpg",null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add = True,null=True)

    def __str__(self):
        return self.name
		
class VisTemp(models.Model):
    user_name = models.ForeignKey(
                    Customer,
                    on_delete=models.CASCADE,)
    title = models.CharField(max_length=200, null=True)
    buy_sell = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add = True,null=True)
    shares_number = models.CharField(max_length=200, null=True)
    course = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
