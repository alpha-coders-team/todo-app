from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}))