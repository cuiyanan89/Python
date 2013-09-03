from blog.models import Customer
from django import forms

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('username','password')
        widgets = {
            'password':forms.PasswordInput,
        }
