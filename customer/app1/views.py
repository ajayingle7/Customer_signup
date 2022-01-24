from django.shortcuts import render
from .models import Customer
from django.http import HttpResponse
# Create your views here.

def homeView(request):
    template_file = 'home.html'
    context = {}

    if request.method=='POST':

        fname = request.POST.get('fn')
        lname = request.POST.get('ln')
        email = request.POST.get('email')
        state = request.POST.get('state')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        mno = request.POST.get('mno')
        password = request.POST.get('pass')

        obj1  =Customer(fname=fname,lname=lname,email=email,city=city,pincode=pincode,mno=mno,password=password)
        obj1.save()

        return HttpResponse('<h1>Data Saved Succesfully.....</h1>')



    return render(request,template_file,context)