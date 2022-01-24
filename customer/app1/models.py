from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Customer(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    state = models.CharField(max_length=50,default='Maharashtra')
    city = models.CharField(max_length=50)
    pincode = models.IntegerField()
    mno = PhoneNumberField()
    password = models.CharField(null=True,max_length=50)


    def __str__(self):
        return f'{self.fname},{self.lname},{self.email},{self.email},{self.city},{self.pincode}{self.mno}'

