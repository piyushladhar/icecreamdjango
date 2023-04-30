from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from .models import Products,Users,Orders
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password']
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a username'}),
            'password': PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter a password'}),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'username': 'Username',
            'password': 'Password',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your first name', 'required': True})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your last name', 'required': True})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your email', 'required': True})
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter a username', 'required': True})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter a password', 'required': True})

    def as_div(self):
        "Returns this form rendered as HTML <div>s."
        return self._html_output(
            normal_row='<div class="form-floating">{label}{field}</div>',
            error_row='%s',
            row_ender='</div>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True)

class LoginForm(ModelForm):
    class Meta:
        model = Users
        fields = ['username','password']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a username'}),
            'password': PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter a password'}),
        }
        labels = {
            'username': 'Username',
            'password': 'Password',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter a username', 'required': True})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter a password', 'required': True})

    def as_div(self):
        "Returns this form rendered as HTML <div>s."
        return self._html_output(
            normal_row='<div class="form-floating">{label}{field}</div>',
            error_row='%s',
            row_ender='</div>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True)

class OrderForm(ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'