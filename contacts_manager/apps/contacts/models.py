from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Organization(models.Model):
	name = models.CharField(max_length=200)

class Person(models.Model):
	organization = models.ForeignKey(Organization)
	name = models.CharField(max_length=200)

class ContactInfo(models.Model):
	person = models.ForeignKey(Person)
	phone_number = models.CharField(max_length=20)
	email_address = models.CharField(max_length=100)
	street_address_1 = models.CharField(max_length=100)
	street_address_2 = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	postal_code = models.CharField(max_length=100)
	country = models.CharField(max_length=100)
