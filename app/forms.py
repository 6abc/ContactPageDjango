# forms.py
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'description', ]
        labels = {'first_name' : 'First Name ','last_name' : 'Last Name ','email' : 'Email ','description' : 'Description ',}
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'you@domain.com'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'required': True, "minlength": 120, 'placeholder': 'Write message'}),
            }