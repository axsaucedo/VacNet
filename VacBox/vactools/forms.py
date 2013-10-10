from django import forms

class ZwitchLinkForm(forms.Form):
    email = forms.EmailField()
    email.required=False
    link = forms.URLField()