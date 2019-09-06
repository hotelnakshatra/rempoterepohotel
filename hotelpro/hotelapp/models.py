from django.db import models

class CustomerData(models.Model):
    date=models.DateTimeField()
    promo=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    orderid=models.IntegerField(unique=True)
    checkin=models.DateField(max_length=100)
    checkout=models.DateField(max_length=100)
    email=models.CharField(max_length=100)
    room=models.CharField(max_length=100)
    amenties=models.CharField(max_length=100)
    amentiestotal=models.IntegerField()
    promodiscount=models.IntegerField()
    total=models.IntegerField()