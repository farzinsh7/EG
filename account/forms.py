from django import forms
from .models import User
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


class ProfileForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super(ProfileForms, self).__init__(*args, **kwargs)

        if user.is_superuser:
            self.fields['username'].disabled = True
            self.fields['email'].disabled = False
        else:
            self.fields['username'].disabled = True
            self.fields['email'].disabled = True

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']