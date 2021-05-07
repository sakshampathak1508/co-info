from django.db import models
from datetime import datetime 
state = (
        ("Andhra Pradesh","Andhra Pradesh"),
        ("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),
        ("Arunachal Pradesh","Arunachal Pradesh"),
        ("Assam","Assam"),
        ("Bihar","Bihar"),
        ("Chandigarh","Chandigarh"),
        ("Chhattisgarh","Chhattisgarh"),
        ("Dadar and Nagar Haveli","Dadar and Nagar Haveli"),
        ("Daman and Diu","Daman and Diu"),
        ("Delhi","Delhi"),
        ("Lakshadweep","Lakshadweep"),
        ("Puducherry","Puducherry"),
        ("Goa","Goa"),
        ("Gujarat","Gujarat"),
        ("Haryana","Haryana"),
        ("Himachal Pradesh","Himachal Pradesh"),
        ("Jammu and Kashmir","Jammu and Kashmir"),
        ("Jharkhand","Jharkhand"),
        ("Karnataka","Karnataka"),
        ("Kerala","Kerala"),
        ("Madhya Pradesh","Madhya Pradesh"),
        ("Maharashtra","Maharashtra"),
        ("Manipur",  "Manipur"),
        ("Meghalaya","Meghalaya"),
        ("Mizoram","Mizoram"),
        ("Nagaland","Nagaland"),
        ("Odisha","Odisha"),
        ("Punjab","Punjab"),
        ("Rajasthan","Rajasthan"),
        ("Sikkim","Sikkim"),
        ("Tamil Nadu","Tamil Nadu"),
        ("Telangana","Telangana"),
        ("Tripura","Tripura"),
        ("Uttar Pradesh","Uttar Pradesh"),
        ("Uttarakhand","Uttarakhand"),
        ("West Bengal","West Bengal"),
    )
oxy_type = (
        ('cylinder','cylinder'),
        ('can', 'can'),
        ('concentrator', 'concentrator'),
        ('refill', 'refill'),
    )
med_names = (
        ('Remdesivir','Remdesivir'),
        ('Fabiflu','Fabiflu'),
        ('Medrol','Medrol'),
        ('Ivermectin','Ivermectin'),
        ('Doxycycline','Doxycycline'),
    )
bed_type = (
        ('Ward','Ward'),
        ('Oxygen','Oxygen'),
        ('ICU', 'ICU'),
    )
blood_group = (
        ('A+','A+'),
        ('A-','A-'),
        ('B+','B+'),
        ('B-','B-'),
        ('O+','O+'),
        ('O-','O-'),
        ('AB+','AB+'),
        ('AB-','AB-'),
    )


# Create your models here.
class Oxygen(models.Model):
    type_of_facility = models.CharField(default="",choices=oxy_type,max_length=200,blank=True)
    name = models.CharField(default="",max_length=200,blank=True)
    city = models.CharField(default="",max_length=200,blank=True)
    state =  models.CharField(default="",choices=state,max_length=200,blank=True)
    address = models.TextField(blank=True)
    number1 = models.CharField(default="",max_length=20,blank=True)
    number2 = models.CharField(default="",max_length=20,blank=True)
    is_available = models.BooleanField(default=False)
    price = models.CharField(default="",max_length=7,blank=True)
    quantity = models.IntegerField(default=0,blank=True)
    time_stamp = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name

class Hospital(models.Model):
    type_of_bed = models.CharField(default="",choices=bed_type,max_length=200,blank=True)
    name = models.CharField(default="",max_length=200,blank=True)
    city = models.CharField(default="",max_length=200,blank=True)
    state =  models.CharField(default="",choices=state,max_length=200,blank=True)
    address = models.TextField(blank=True)
    number1 = models.CharField(default="",max_length=20,blank=True)
    number2 = models.CharField(default="",max_length=20,blank=True)
    number_of_beds = models.IntegerField(default=0,blank=True)
    is_available = models.BooleanField(default=False)
    time_stamp = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return self.name

class Plasma(models.Model):
    blood_group = models.CharField(default="",choices=blood_group,max_length=200,blank=True)
    name = models.CharField(default="",max_length=200,blank=True)
    city = models.CharField(default="",max_length=200,blank=True)
    state =  models.CharField(default="",choices=state,max_length=200,blank=True)
    number1 = models.CharField(default="",max_length=20,blank=True)
    number2 = models.CharField(default="",max_length=20,blank=True)
    days_since_recovery = models.IntegerField(default=0,blank=True)
    is_available = models.BooleanField(default=False)
    time_stamp = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name

class Medicine(models.Model):
    medicine_name = models.CharField(default="",choices=med_names,max_length=200,blank=True) 
    name = models.CharField(default="",max_length=200,blank=True)
    city = models.CharField(default="",max_length=200,blank=True)
    state =  models.CharField(default="",choices=state,max_length=200,blank=True)
    address = models.TextField(blank=True)
    number1 = models.CharField(default="",max_length=20,blank=True)
    number2 = models.CharField(default="",max_length=20,blank=True)
    quantity = models.IntegerField(default=0,blank=True)
    price = models.CharField(default="",max_length=7,blank=True)
    is_available = models.BooleanField(default=False)
    time_stamp = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.name