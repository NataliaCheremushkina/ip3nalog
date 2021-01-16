from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100, label='',
                           widget=forms.TextInput(attrs={'class': "form-input", 'placeholder': 'Ваше имя'}))
    email = forms.EmailField(label='',
                             widget=forms.TextInput(attrs={'class': "form-input", 'placeholder': 'Email'}))
