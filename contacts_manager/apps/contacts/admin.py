from django.contrib import admin

# Register your models here.
from .models import Person, Organization
admin.site.register(Person)
admin.site.register(Organization)