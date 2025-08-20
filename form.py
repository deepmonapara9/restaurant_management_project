from django import forms
from .models import Contact

class ContactForm(form.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email']