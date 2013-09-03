from blog.models import User,Foodtype,Food
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password')
        widgets = {
            'password':forms.PasswordInput,
        }
