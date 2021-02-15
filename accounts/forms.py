from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from accounts.models import User


# class RegisterUserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('email', 'full_name', 'dateofbirth', 'phone', 'password')
#
#         widgets = {
#             # 'email':forms.EmailField(),
#             'phone': forms.NumberInput(),
#             'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', }),
#         }
#         # labels = {
#         #     'password':'رمز عبور',
#         # }
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password"])
#         if commit:
#             user.save()
#         return user


# class RegisterFormAdmin(RegisterUserForm):
#     class Meta:
#         widgets = {
#             # 'email':forms.EmailField(),
#             'phone': forms.NumberInput(
#                 attrs={'class': 'form-control', 'placeholder': '09 - - - - - - - - -', 'type': 'tel', 'maxlength': '11',
#                        'minlength': '11'}),
#             'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام و نام خانواگی', }),
#             'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', }),
#         }


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Password confirmation'), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'full_name', 'dateofbirth', 'phone','idcode', 'is_active', 'is_admin')

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
        fields = ('email', 'full_name', 'dateofbirth', 'phone', 'idcode', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}), label=_('Email'))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label=_('Password'))



