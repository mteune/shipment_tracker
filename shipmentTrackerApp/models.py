from django.db import models
import re
import bcrypt
from .models import *



class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        #length of 1st name
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters long!"
        #length of last name
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters long!"
        #email matches format
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['email']) == 0:
            errors['email'] = "You must enter an email!"
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Must be a valid email!"
        #email is unique
        current_users = User.objects.filter(email=postData['email'])
        if len(current_users) > 0:
            errors['duplicate'] = "That email is already in use!"
        #password was entered (less than 8)
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 charachters long!"
        if postData['password'] != postData['confirm_password']:
            errors['mismatch'] = "Your passwords do not match!"
        return errors

    def login_validator(self, postData):
        errors = {}
        existing_user = User.objects.filter(email=postData['email'])
        if len(existing_user) != 1:
            errors['email'] = "User does not exist."
        #email has been entered
        if len(postData['email']) == 0:
            errors['email'] = "Email must be entered!"
        #password has been entered
        if len(postData['password']) < 8:
            errors['password'] = "Password must be 8 charachters!"
        #if the email and password match
        elif bcrypt.checkpw(postData['password'].encode(), existing_user[0].password.encode()) != True:
            errors['mismatch']="Email and password do not match!"
        return errors

    def profile_validator(self, postData):
        errors = {}
        #length of 1st name
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters long!"
        #length of last name
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters long!"
        #email matches format
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['email']) == 0:
            errors['email'] = "You must enter an email!"
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Must be a valid email!"
        return errors



class ShipManager(models.Manager): 
    def ship_validator(self, postData):
        errors = {}
        if postData['date_booked'] == '':
            errors['date_booked'] = "You must enter a date booked!"
        DATE_REGEX = re.compile(r'[0-9]{2}(?:[0-9]{2})?-[0-1][0-9]-[0-3][0-9]')
        if not DATE_REGEX.match(postData['date_booked']):
            errors['date_booked'] = "You must enter a date booked!"
        if len(postData['client']) < 1:
            errors['client'] = "Please enter client name."
        if len(postData['batch']) < 1:
            errors['batch'] = "Please enter batch name."
        if len(postData['volume']) < 1:
            errors['volume'] = "Please enter volume."       
        if len(postData['basis']) < 1:
            errors['city'] = "Destination must be at least 3 charachters long!"        
        if postData['ship_start'] == '':
            errors['ship_start'] = "You must enter a start date!"
        DATE_REGEX = re.compile(r'[0-9]{2}(?:[0-9]{2})?-[0-1][0-9]-[0-3][0-9]')
        if not DATE_REGEX.match(postData['ship_start']):
            errors['ship_start'] = "You must enter a start date!"
        if postData['ship_end'] == '':
            errors['ship_end'] = "You must enter an end date!"
        DATE_REGEX = re.compile(r'[0-9]{2}(?:[0-9]{2})?-[0-1][0-9]-[0-3][0-9]')
        if not DATE_REGEX.match(postData['ship_end']):
            errors['ship_end'] = "You must enter an end date!"
        return errors


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    profile_pic = models.ImageField(default="default.png", blank=True)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
#   ships = a list of apps associated with a given user

class Ship(models.Model):
    date_booked = models.DateField(blank=True, null=True)
    client = models.CharField(max_length=45)
    batch = models.CharField(max_length=45)
    volume = models.CharField(max_length=45)
    basis = models.CharField(max_length=45)
    ship_start = models.DateField(blank=True, null=True)
    ship_end = models.DateField(blank=True, null=True)
    vessel_name = models.CharField(max_length=45, blank=True, null=True)
    last_day_pricing = models.DateField(blank=True, null=True)
    eta_gh = models.DateField(blank=True, null=True)
    etd_gh = models.DateField(blank=True, null=True)
    eta_disport = models.DateField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, related_name="ships", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShipManager()

    