from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from accounts.models import User
from pytz import timezone
from datetime import datetime as dt
from django.conf import settings


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label=_('Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(
        label=_('Password confirmation'), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'email_confirm', 'full_name', 'dateofbirth', 'phone', 'phone_confirm', 'idcode', 'is_active',
                  'is_admin')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'email_confirm', 'full_name', 'dateofbirth', 'phone', 'phone_confirm', 'idcode', 'is_active',
                  'is_admin')

    def clean_password(self):
        return self.initial["password"]


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Email', 'dir': 'ltr'}),
        label=_('Email'))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password', 'dir': 'ltr'}),
        label=_('Password'))


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password', 'dir': 'ltr', 'onChange': 'onChange()',
               'minlength': '8'}))
    password2 = forms.CharField(label=_('Password confirmation'),
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Re-Enter Password',
                                           'dir': 'ltr', 'onChange': 'onChange()'}))

    class Meta:
        model = User
        fields = ('email', 'full_name', 'dateofbirth', 'idcode', 'phone')

        widgets = {
            # 'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@gmail.com', 'dir': 'ltr', 'oninvalid':"setCustomValidity('Please enter your email address')"}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'example@gmail.com', 'dir': 'ltr'}),
            'full_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': _('First And Last Name'), 'invalid': 'fuulNameJS()',
                       'lang': 'en'}),
            'phone': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': '09 - - - - - - - - -', 'type': 'tel', 'maxlength': '11',
                       'minlength': '11', 'dir': 'ltr', 'onkeypress': 'return isNumber(event)'}),
            'idcode': forms.NumberInput(
                attrs={'class': 'form-control', 'type': 'tel', 'placeholder': '1234567890', 'maxlength': '10',
                       'minlength': '10', 'dir': 'ltr', 'onkeypress': 'return isNumber(event)'}),
        }

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        tz = timezone(settings.TIME_ZONE)
        timDel = dt.now(tz)
        # DateNow = timDel.strftime("%Y/%m/%d %H:%M:%S")
        YearNow = int(timDel.strftime("%Y"))
        YEAR_CHOICES = range(YearNow, 1959, -1)
        MONTH_CHOICES = {
            1: 'January', 2: 'February', 3: 'March', 4: 'April',
            5: 'May', 6: 'June', 7: 'July', 8: 'August',
            9: 'September', 10: 'October', 11: 'November', 12: 'December'}
        self.fields['dateofbirth'] = forms.DateField(required=True,
                                                     widget=forms.SelectDateWidget(empty_label=['Year', 'Month', 'Day'],
                                                                                   years=YEAR_CHOICES,
                                                                                   months=MONTH_CHOICES),
                                                     label=_('Date Of Birth'))

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        else:
            return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class ForgetForm(forms.Form):
    email = forms.EmailField(label=_('Email'), widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'example@gmail.com', 'dir': 'ltr'}))
    idcode = forms.IntegerField(label=_('ID Code'), widget=forms.NumberInput(
        attrs={'class': 'form-control', 'type': 'tel', 'placeholder': '1234567890', 'maxlength': '10',
               'minlength': '10', 'dir': 'ltr', 'onkeypress': 'return isNumber(event)'}))


class ResetPassword(forms.Form):
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password', 'dir': 'ltr', 'onChange': 'onChange()',
               'minlength': '8'}))
    password2 = forms.CharField(label=_('Password confirmation'),
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Re-Enter Password',
                                           'dir': 'ltr', 'onChange': 'onChange()'}))

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        else:
            return password2


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'full_name', 'dateofbirth', 'idcode', 'phone']

        widgets = {
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'example@gmail.com', 'dir': 'ltr',
                       'readonly': 'readonly'}),
            'full_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': _('First And Last Name'), 'invalid': 'fuulNameJS()',
                       'lang': 'en'}),
            'idcode': forms.NumberInput(
                attrs={'class': 'form-control', 'type': 'tel', 'placeholder': '1234567890', 'maxlength': '10',
                       'minlength': '10', 'dir': 'ltr', 'onkeypress': 'return isNumber(event)'}),
            'phone': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': '09 - - - - - - - - -', 'type': 'tel', 'maxlength': '11',
                       'minlength': '11', 'dir': 'ltr', 'onkeypress': 'return isNumber(event)'}),
        }

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        usr = kwargs['instance']
        phone_confirm = usr.phone_confirm
        tz = timezone(settings.TIME_ZONE)
        timDel = dt.now(tz)
        # DateNow = timDel.strftime("%Y/%m/%d %H:%M:%S")
        YearNow = int(timDel.strftime("%Y"))
        YEAR_CHOICES = range(YearNow, 1959, -1)
        MONTH_CHOICES = {
            1: 'January', 2: 'February', 3: 'March', 4: 'April',
            5: 'May', 6: 'June', 7: 'July', 8: 'August',
            9: 'September', 10: 'October', 11: 'November', 12: 'December'}
        self.fields['dateofbirth'] = forms.DateField(required=True,
                                                     widget=forms.SelectDateWidget(empty_label=['Year', 'Month', 'Day'],
                                                                                   years=YEAR_CHOICES,
                                                                                   months=MONTH_CHOICES),
                                                     label=_('Date Of Birth'))
        if phone_confirm:
            self.fields['phone'] = forms.IntegerField(label=_('Phone Number'), widget=forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': '09 - - - - - - - - -', 'type': 'tel', 'maxlength': '11',
                       'minlength': '11', 'dir': 'ltr', 'readonly': 'readonly'}))


class VerifyForm(forms.Form):
    code = forms.IntegerField(label=_('Confirm Code'), widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': _('Confirm Code'), 'type': 'tel', 'style': 'text-align:center'}))
