from django import forms
from Landing_page.models import ContactUs


class ContactForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactForms, self).__init__(*args, **kwargs)
        self.fields['subject'].disabled = True
        self.fields['name'].disabled = True
        self.fields['email'].disabled = True
        self.fields['message'].disabled = True

    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject', 'message', 'status']