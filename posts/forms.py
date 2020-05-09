from django import forms
from .models import User, Image, Post
#forms
class UserCreateForm(forms.ModelForm):
    #set password and confirm password field
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username','first_name','last_name','password')

    def clean(self):
        """
        checks if the 'cleaned' password and confirm_password
        are the same, if not, raises an error
        """
        cleaned_data = super(UserCreateForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm password does not match"
            )
    def save(self):
        """
        assigns the user password using the set_password method
        as normal assignment does not encrypt or saves
        the password
        """
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length =100,widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
