from django.shortcuts import render,redirect
import datetime
import random
from django.http.response import HttpResponse
from .models import CustomerData

def homeview(request):
    if request.method=="POST":
        date=datetime.datetime.now()
        orderid=random.randint(200000,900000)
        checkindate=request.POST.get('checkin')
        checkoutdate=request.POST.get('checkout')
        name=request.POST.get('name')
        name=str(name).title()
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        promo=request.POST.get('promo')
        room=request.POST.get('room')
        amenties1=request.POST.get('amenties1')
        amenties2=request.POST.get('amenties2')
        amenties3=request.POST.get('amenties3')
        amentiestotal=0
        if amenties1:
            amentiestotal+=1000
        if amenties2:
            amentiestotal+=250
        if amenties3:
            amentiestotal+=50
        if amenties1:
            pass
        else:
            amenties1=' '
        if amenties2:
            pass
        else:
            amenties2=' '
        if amenties3:
            pass
        else:
            amenties3=' '
        amenties=amenties1+' '+amenties2+' '+amenties3
        roomtotal=0
        if room=='Ordinary':
            roomtotal+=1500
        elif room=='Deluxe':
            roomtotal+=2500
        elif room=='Ordinary':
            roomtotal+=5000

        total=roomtotal+amentiestotal
        promodiscount=0
        if promo=='FIRST50':
            promodiscount+=total*50//100
        total=total-promodiscount

        data=CustomerData(date=date,name=name,mobile=mobile,email=email,orderid=orderid,checkin=checkindate,
                          checkout=checkoutdate,room=room,amenties=amenties,amentiestotal=amentiestotal,
                          promodiscount=promodiscount,total=total,promo=promo)
        data.save()
        return redirect(bookingconfirm)

    else:
        return render(request, 'home.html')

def bookingconfirm(request):
    if request.method=="GET":
        b=CustomerData.objects.raw('SELECT * FROM hotelapp_customerdata LIMIT 1')
        m=CustomerData.objects.raw('SELECT * FROM hotelapp_customerdata ORDER BY ID DESC LIMIT 1')


        #y=CustomerData.objects.raw('SELECT * FROM hotelapp_customerdata')[0]
        #x=CustomerData.objects.raw('SELECT * FROM hotelapp_customerdata WHERE orderid = %s', [orderid])
        return render(request,'confirm.html',{'data':m})
    else:
        pass

def cancelbooking(request):
    if request.method=="POST":
        bookingid=request.POST.get('bookingid')
        cancellationdata=CustomerData.objects.all().filter(orderid=bookingid)

        cancelled=request.POST.get('cancelcheckbox')
        if cancelled=='agree':
            x=CustomerData.objects.filter(orderid=bookingid)
            x.delete()
        return render(request, 'cancel.html', {'boookingid':bookingid,'cancellationdata':cancellationdata,'cancelled':cancelled})
    else:
        bookingid = request.POST.get('bookingid')
        data=CustomerData.objects.all().filter(orderid=bookingid)
        #x=CustomerData.objects.raw('SELECT * FROM hotelapp_customerdata WHERE orderid = %s', [bookingid])
        return render(request, 'cancel.html',{'data':data})