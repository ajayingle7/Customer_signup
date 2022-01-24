from django.contrib import admin
from .models import Customer
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['fname','lname','email','state','city','pincode','mno']

admin.site.register(Customer,CustomerAdmin)
