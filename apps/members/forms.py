from django import forms
from django.db import models
from models import *
from apps.geo.models import Country


class ProfileForm(forms.Form):
	username		= forms.CharField(max_length=50)
	email			= forms.EmailField(max_length=50)
	first_name		= forms.CharField(max_length=50)
	last_name		= forms.CharField(max_length=50)
	gender	 		= forms.ChoiceField(choices=settings.ENUMS["GENDER"])
	dob 			= forms.DateField()
	
	zipcode 		= forms.CharField(max_length=7,required=False)
	street_line_1	= forms.CharField(max_length=100,required=False)
	street_line_2	= forms.CharField(max_length=100,required=False)
	city			= forms.CharField(max_length=25,required=False)
	state			= forms.CharField(max_length=20,required=False)
	country			= forms.ChoiceField(choices=Country.list_for_dropdown(),required=False)
	

class SignupForm(forms.Form):
	first_name		= forms.CharField(max_length=50)
	last_name		= forms.CharField(max_length=50)
	username		= forms.CharField(max_length=30)
	email			= forms.EmailField(max_length=50)
	email2			= forms.EmailField(max_length=50)
	password		= forms.CharField(max_length=30)
	gender	 		= forms.ChoiceField(choices=settings.ENUMS["GENDER"])
	dob 			= forms.DateField()

class LoginForm(forms.Form):
	username		= forms.CharField(max_length=30)
	password		= forms.CharField(max_length=30)

class InvitationForm(forms.Form):
	email			= forms.EmailField(max_length=50)
	first_name		= forms.CharField(max_length=50,required=False)
	last_name		= forms.CharField(max_length=50,required=False)
	
