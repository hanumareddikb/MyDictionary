from django import forms

# create your forms here
# form to register or signup user
class SignupForm(forms.Form):
    username = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Username*','style':'width:300px'}))
    email = forms.EmailField(label='',widget=forms.EmailInput(attrs={'placeholder':'Email*','style':'width:300px'}))
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'Password*','style':'width:300px'}))
    confirm_password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password*','style':'width:300px'}))

# form to log in user
class LoginForm(forms.Form):
    email = forms.EmailField(label='',widget=forms.EmailInput(attrs={'placeholder':'Email*','style':'width:300px'}))
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'Password*','style':'width:300px'}))