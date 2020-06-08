from django import forms
from .models import tea,playe,player
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:

	    model=User
	    fields = ["username", "email", "password1", "password2"]
# from .models import Employee  
# class EmployeeForm(forms.ModelForm):  
#     class Meta:  
#         model = Employee  
#         fields = "__all__"  

class teams(forms.ModelForm):
    class Meta:
        model = tea
        fields = "__all__"


class players(forms.ModelForm):
    class Meta:
        model = playe
        fields = "__all__"   
class SearchForm(forms.Form):
    q=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','maxlength':'30','placeholder':'Search'}))  

class play(forms.ModelForm):
    class Meta:
        model = player
        fields = "__all__"   
