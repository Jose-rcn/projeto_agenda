from django.core.exceptions import ValidationError
from django import forms
from contact.models import Contact


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Que bagunça'}),
        label='Primeiro Nome',
        help_text='Escreva o primeiro nome'
        )

    class Meta:
        model = Contact
        fields = 'first_name', 'last_name', 'phone'

    def clean(self):
        if self.cleaned_data.get('first_name') == 'cleiton':
            self.add_error('first_name',
                           ValidationError('Nome feio', code='invalid'))
            self.add_error('first_name',
                           ValidationError('aaaaaaaaaaaaaa', code='invalid'))