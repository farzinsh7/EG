from django import forms
from .models import ContactForm


class ContactFormClass(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ('name', 'email', 'subject', 'message')
        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Name', 'name':'name', 'type':'text'}),
        'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Email', 'name':'email'}),
        'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Subject', 'name':'Subject'}),
        'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Enter your message here...', 'name':'Message', 'cols':'30', 'rows':'10'}),
        }