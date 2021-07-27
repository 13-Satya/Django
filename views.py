from django.shortcuts import render
from django.http import HttpResponseRedirect
import random, string, datetime
from oyo.models import Customer, Manager,Hotel, Bookings, Employee, Rooms
from django.contrib import messages
c=0
h=0
# create a function
def home(request):
    return render(request, 'hoome.html')
def manager(request):
    return render(request,'manager.html')
def manager_login(request):
    if request.method=='POST':
        log=Manager()
        log.m_id=request.POST.get('m_id')
        log.password=request.POST.get('password')
        if Manager.objects.filter(m_id=log.m_id):
            if Manager.objects.filter(password=log.password):
                return render(request,'manager.html')
            else:
                messages.success(request,'Incorrect password')
        else:
            messages.success(request,'Invalid m_id')
        return render(request,'manager_login.html')
    else:
        return render(request,'manager_login.html')

def manager_sign(request):
    if request.method=='POST':
        dat=Manager()
        dat.m_id=random.randint(0,100)
        dat.h_id=request.POST.get('h_id')
        dat.name=request.POST.get('name')
        dat.email=request.POST.get('email')
        dat.contact=request.POST.get('contact')
        dat.password=request.POST.get('password')
        dat.save()
        messages.success(request,'M_ID is '+str(dat.m_id))
        return render(request,'manager_sign.html')
    else:
        return render(request,'manager_sign.html')
def booking(request):
    if request.method=='POST':
        dat=Bookings()
        r=Rooms()
        bill=0
        price=0
        no=request.POST.get('number')
        dat.h_id=request.POST.get('h_id')
        dat.book_id=random.randint(10**7,(10**8)-1)
        dat.c_id=request.POST.get('c_id')
        dat.check_in=request.POST.get('check_in')
        dat.check_out=request.POST.get('check_out')
        dat.room=request.POST.get('room')
        same=Rooms.objects.filter(h_id=dat.h_id)
        for ro in same:
            if ro.type == dat.room:
                price=ro.price
                break
        bill=int(str(price))*int(str(request.POST.get('number')))
        dat.save()
        messages.success(request,'BOOKING ID is '+str(dat.book_id))
        messages.success(request,'BILL is '+str(bill))
        return render(request,'booking_page.html')
    else:
        return render(request,'booking_page.html')
def customer_signup(request):
    if request.method=='POST':
        dat=Customer()
        dat.c_id=random.randint(0,100)
        dat.name=request.POST.get('name')
        dat.email=request.POST.get('email')
        dat.contact=request.POST.get('contact')
        dat.password=request.POST.get('password')
        
        dat.save()
        messages.success(request,'C_ID is '+str(dat.c_id))
        return render(request,'customer.html')
    else:
        return render(request,'customer.html')
def customer_login(request):
    if request.method=='POST':
        log=Customer()
        log.c_id=request.POST.get('c_id')
        log.password=request.POST.get('password')
        c=log.c_id
        if Customer.objects.filter(c_id=log.c_id):
            if Customer.objects.filter(password=log.password):
                all=Bookings.objects.all().filter(c_id=log.c_id)
                context={'all':all}
                return render(request,'cust.html',context)
            else:
                messages.success(request,'Incorrect password')
        else:
            messages.success(request,'Invalid c_id')
        return render(request,'cust.html')
    else:
        return render(request,'customer_login.html')
def customer_home(request):
    return render(request,'cust.html')
def all_booking(request):
    all=Bookings.objects.all()
    context={'all':all}
    return render(request,'all_booking.html',context)
def all_employee(request):
    all=Employee.objects.all()
    context={'all':all}
    return render(request,'all_employee.html',context)

def view_hotel(request):
    all=Hotel.objects.all()
    context={'all':all}
    return render(request,'view_hotel.html',context)
def search_cust(request):
    if request.method=="POST":
        log=Customer()
        log.name=request.POST.get('name')
        log.c_id=request.POST.get('c_id')
        if Customer.objects.filter(name=log.name.lower()) or Customer.objects.filter(c_id=log.c_id):
            messages.success(request,'Login Granted')
        else:
            messages.success(request,'Database could not find any of those')
        return render(request,'search_cust.html')
    else:
        return render(request,'search_cust.html')
