from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100)
    mname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    # date_posted = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
            return self.contact_id + '_' + self.fname

class address(models.Model):
    address_id = models.AutoField(primary_key=True)
    contact_id = models.ForeignKey(contact,on_delete=models.CASCADE)
    address_type = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)

    def __str__(self):
            return self.address_id + '_' + self.contact_id

    class Meta:
        get_latest_by = 'address_id'

class phone(models.Model):
    phone_id = models.AutoField(primary_key=True)
    contact_id = models.ForeignKey(contact,on_delete=models.CASCADE)
    phone_type = models.CharField(max_length=100)
    area_code = models.CharField(max_length=200)
    number = models.CharField(max_length=15)
    
    def __str__(self):
            return self.phone_id + '_' + self.contact_id

    class Meta:
        get_latest_by = 'phone_id'

    

class date(models.Model):
    date_id = models.AutoField(primary_key=True)
    contact_id = models.ForeignKey(contact,on_delete=models.CASCADE)
    date_type = models.CharField(max_length=100)
    date = models.DateField()
    
    def __str__(self):
            return self.date_id + '_' + self.contact_id






