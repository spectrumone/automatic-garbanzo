from django import forms


class EmailSendForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    subject = forms.CharField(max_length=50)
    message = forms.CharField(max_length=200)
