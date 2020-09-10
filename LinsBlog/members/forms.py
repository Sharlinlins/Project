from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from myblog.models import Profile

class ProfilePageForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url')

        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            # 'profile_pic': forms.TextInput(attrs={'class': 'form-control'}),
            'website_url': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'})
        }

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label='Email')
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label='First Name')
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Last Name')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
    

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label='Email')
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label='First Name')
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Last Name')
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Username')
    last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Last Login')
    is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}), label='Is SuperUser')
    is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}), label='Is Staff')
    is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}), label='Is Active')
    date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Date Joined')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined')

    
class EditProfileStaffForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label='Email')
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label='First Name')
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Last Name')
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Username')
    last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Last Login', disabled=True)
    date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Date Joined', disabled=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'last_login', 'date_joined')
    
class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}), label='Old Password')
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}), label='New Password')
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}), label='Confirm New Password')

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

class EditProfilePageForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url')

        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            # 'profile_pic': forms.TextInput(attrs={'class': 'form-control'}),
            'website_url': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'})
        }