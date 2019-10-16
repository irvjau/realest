
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)    #makes email mandatory 

    class Meta: 
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2'
        )

        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
            'password2': None,
        }

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']        # prevents sql injection
        user.last_name = self.cleaned_data['last_name']


        if commit:
            user.save()

        return user