from django.db import models

# Create your models here.
class Hotel(models.Model):
    name=models.CharField(max_length=20)
    h_id=models.IntegerField()
    locality=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    country=models.CharField(max_length=30)
    description=models.TextField()
    class Meta:
        db_table="oyo_hotel"

class Rooms(models.Model):
    h_id=models.IntegerField()
    type=models.CharField(max_length=20)
    price=models.IntegerField()
    description=models.TextField()
    class Meta:
        db_table="oyo_rooms"

class Manager(models.Model):
    name=models.CharField(max_length=20)
    h_id=models.IntegerField()
    m_id=models.IntegerField()
    email=models.CharField(max_length=40)
    contact=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    class Meta:
        db_table="oyo_manager"

class Employee(models.Model):
    name=models.CharField(max_length=20)
    h_id=models.IntegerField()
    e_id=models.IntegerField()
    area=models.CharField(max_length=15)
    email=models.CharField(max_length=40)
    contact=models.CharField(max_length=10)
    class Meta:
        db_table="oyo_employee"

class Bookings(models.Model):
    h_id=models.IntegerField()
    book_id=models.IntegerField()
    c_id=models.IntegerField()
    check_in=models.DateTimeField()
    check_out=models.DateTimeField()
    room=models.CharField(max_length=20)
    class Meta:
        db_table="oyo_bookings"

class Customer(models.Model):
    c_id=models.IntegerField()
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=40)
    contact=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    class Meta:
        db_table="oyo_customer"

class Payment(models.Model):
    book_id=models.IntegerField()
    transact_no=models.IntegerField()
    amount=models.IntegerField()
    date=models.DateTimeField()

class Add_ons(models.Model):
    book_id=models.IntegerField()
    c_id=models.IntegerField()
    charge=models.IntegerField()
    service=models.CharField(max_length=15)
