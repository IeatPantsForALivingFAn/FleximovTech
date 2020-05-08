from django import forms
from .models import User, Image, Post
#forms
class UserCreateForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username','first_name','last_name','password')

    def clean(self):
        cleaned_data = super(UserCreateForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm password does not match"
            )
    def save(self):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length =100,widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

# class PostCreateForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title','image']

#
# class ImageCreateForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = ['image_field']
#
#     def __init__(self,*args,**kwargs):
#         uploaded_by = kwargs.pop('uploaded_by', None)
#         super().__init__(*args, **kwargs)
#         self.fields['uploaded_by'] = User.objects.get(pk =request.pk)
