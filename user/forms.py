from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from user.models import Profile, Comment


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label="Username",
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'username ...'
                               }))

    first_name = forms.CharField(label="First Name",
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control',
                                     'placeholder': 'first name ...'
                                 }))

    last_name = forms.CharField(label="Last Name",
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'last name ...'
                                }))

    email = forms.EmailField(label="Email Address",
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'email ...'
                             }))

    password1 = forms.CharField(label="Create password",
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'create password ...'
                                }))

    password2 = forms.CharField(label="Confirm password",
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'confirm password ...'
                                }))

    class Meta:
        model = User

        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username",
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'username ...'
                               }))

    password = forms.CharField(label="Create password",
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'create password ...'
                                }))

class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=225, required=False, label="First Name")
    last_name = forms.CharField(max_length=225, required=False, label="Last Name")
    email = forms.EmailField(required=False, label="Email")

    class Meta:
        model = Profile
        fields = ['photo', 'phone', 'country', 'city', 'bio', 'job']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:

            self.fields[field].widget.attrs.update({'class': 'form-control'})


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Оставьте ваш комментарий здесь...'}),
        }

