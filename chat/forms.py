from django import forms


class MessageForm(forms.Form):
    message = forms.CharField(max_length=10000, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={
        'class': '',
        'multiple': True
    }))
