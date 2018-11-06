from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Participant

class  ParticipantCreationForm(UserCreationForm):
    class Meta:
        model = Participant
        fields = ('username', 'email', 'first_name', 
        'last_name', 'contact_number'
        )