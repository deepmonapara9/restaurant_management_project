from django import forms
from .models import Contact

class ContactForm(form.ModelForm):
    name = forms.CharField(max_length=200, label="Deep")
    email = forms.EmailField(label="abc@gmail.com")
    message = forms.CharField(widget=forms.Textarea, label="Yello!")

    class Meta:
        model = Contact
        fields = ['name', 'email']