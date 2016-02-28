from django.forms import ModelForm
from .models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = [
            'first_name',
            'last_name',
            'street_address_1',
            'street_address_2',
            'city',
            'state',
            'postal_code',
            'country',
            'email_address',
            'phone_number',
            'organization',
        ]
