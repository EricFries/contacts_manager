from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Organization(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Person(models.Model):
	organization = models.ForeignKey(Organization, null=True, blank=True)
	name = models.CharField(max_length=200)
	phone_number = models.CharField(max_length=20, null=True, blank=True)
	email_address = models.EmailField(max_length=100, null=True, blank=True)
	street_address_1 = models.CharField(max_length=100, null=True, blank=True)
	street_address_2 = models.CharField(max_length=100, null=True, blank=True)
	city = models.CharField(max_length=100, null=True, blank=True)
	state = models.CharField(max_length=100, null=True, blank=True)
	postal_code = models.CharField(max_length=100, null=True, blank=True)
	country = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return self.name