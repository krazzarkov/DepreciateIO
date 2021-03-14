from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.choices import *
#from main.models import Phones

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data["email"]
		if commit:
			user.save() #saves to db
		return user


CHOICES = PHONE_CHOICES

class ChoosePhone(forms.Form):
	phone = forms.ChoiceField(choices=CHOICES)