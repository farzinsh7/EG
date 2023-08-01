from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}),
        label='Name',
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
        label='Email',
    )
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'form-control'}),
        label='Subject',
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter your message here...', 'class': 'form-control', 'name':'Message', 'cols':'30', 'rows':'10'}),
        label='Message'
    )