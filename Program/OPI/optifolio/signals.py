from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Customer

def customer_profile(sender, instance, created, **kwargs):
    if created:
            group = Group.objects.get(name='customer')
            instance.groups.add(group)

            Customer.objects.create(
                user=instance,
                name=instance.username,
            )
            print('Profile created')

def portfolio(sender, instance, created, **kwargs):
    if created:
        Portfolio.objects.create(
            portfolio=instance,
            name=instance.name
        )
    print('Portfolio created')

post_save.connect(customer_profile, sender=User)
post_save.connect(portfolio, sender=Portfolio)






