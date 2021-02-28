from django import forms
from base.models import Contact, Newsletters


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'message')

        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'data-error': 'لطفا نام خود را وارد کنید', 'placeholder': 'نام شما',
                       'style': 'color:#00FF3E'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'data-error': 'لطفا ایمیل خود را وارد کنید',
                                             'placeholder': 'ایمیل شما', 'style': 'color:#00FF3E'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'data-error': 'لطفا شماره خود را وارد کنید',
                                              'placeholder': 'شماره تماس شما', 'maxlength': '11',
                                              'minlength': '11', 'type': 'tel', 'style': 'color:#00FF3E'}),
            'message': forms.Textarea(
                attrs={'class': 'form-control', 'data-error': 'پیام خود را بنویسید', 'placeholder': 'پیام شما',
                       'style': 'color:#00FF3E'})
        }


class NewslettersForm(forms.ModelForm):
    class Meta:
        model = Newsletters
        fields = ('email',)

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'data-error': 'لطفا ایمیل خود را وارد کنید',
                                             'placeholder': 'Your Email'})
        }
