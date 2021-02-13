from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from accounts.models import User


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'full_name', 'dateofbirth', 'phone', 'password')

        widgets = {
            # 'email':forms.EmailField(),
            'phone': forms.NumberInput(),
            'password': forms.PasswordInput()
        }
        labels = {
            'password':'رمز عبور',
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.changed_data['password'])
        if commit:
            user.save()
        return user

class RegisterFormAdmin(RegisterUserForm):
    class Meta:
        widgets = {
            # 'email':forms.EmailField(),
            'phone': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': '09 - - - - - - - - -', 'type': 'tel', 'maxlength': '11',
                       'minlength': '11'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام و نام خانواگی', }),
            'password': forms.PasswordInput(),
        }

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    labels = {
        'password':'رمز عبور'
    }
    class Meta:
        model = User
        fields = ('email', 'full_name', 'dateofbirth', 'phone','password', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial("password")

