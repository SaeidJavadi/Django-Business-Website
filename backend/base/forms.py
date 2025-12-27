from django import forms
from base.models import Contact, Newsletters


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'message')

        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'data-error': 'Please enter your name', 'placeholder': 'Your name',
                       'style': 'color:#00FF3E'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'data-error': 'Please enter your email',
                                             'placeholder': 'Your email', 'style': 'color:#00FF3E'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'data-error': 'Please enter your phone number',
                                              'placeholder': 'Your contact number', 'maxlength': '11',
                                              'minlength': '11', 'type': 'tel', 'style': 'color:#00FF3E'}),
            'message': forms.Textarea(
                attrs={'class': 'form-control', 'data-error': 'Please write your message', 'placeholder': 'Your message',
                       'style': 'color:#00FF3E'})
        }


class NewslettersForm(forms.ModelForm):
    class Meta:
        model = Newsletters
        fields = ('email',)

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'data-error': 'Please enter your email',
                                             'placeholder': 'Your Email'})
        }
