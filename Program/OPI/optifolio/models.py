from django.db import models
from djmoney.models.fields import MoneyField
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
		
class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
    

class Portfolio(models.Model):
    user_id = models.ForeignKey(User)
    name = models.CharField(max_length=200, null = True, blank=True)
    is_historical = models.BooleanField(default=False)

class PortfolioCompany(models.Model):
    id_portfolio = models.ForeignKey(Portfolio)
    id_company = models.ForeignKey(Company)
    amount = models.Int()

class Company(models.Model):
    name = models.CharField(max_length=200)
    sector = models.CharField(max_length=200) 
    consensus = models.CharField(max_length=50) #buy/sell/hold

class Purchase(models.Model):
        id_portfolio = models.ForeignKey(Portfolio)
        id_company = models.ForeignKey(Company)
        b_s = models.CharField(max_lenght=1)
        amount = models.FloatField()
        date = models.DateField()
        price = MoneyField(decimal_places=2, default=0, default_currency='USD', max_digits=11)
        fare = MoneyField(decimal_places=2, default=0, default_currency='USD', max_digits=11)

#historii chyba nie trzeba bo można ściągnąć używając api