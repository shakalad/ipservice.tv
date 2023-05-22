from django import forms
from .models import Application, ApplicationKZ


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name_surname', 'phone_number', 'town']
        widgets = {
            'name_surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'სახელი გვარი'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ტელეფონის ნომერი'}),
            'town': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ქალაქი'}),
        }

        error_messages = {
            'name_surname': {
                'required': 'სავალდებულო ველი',
            },
            'phone_number': {
                'required': 'სავალდებულო ველი',
            },
            'town': {
                'required': 'სავალდებულო ველი',
            },
        }

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        self.fields['name_surname'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['town'].widget.attrs.update({'class': 'form-control'})

    def is_valid(self):
        for field in self.errors:
            self[field].field.widget.attrs.update({'class': 'form-control is-invalid'})
        return super(ApplicationForm, self).is_valid()


# KZ FORM
class ApplicationFormKZ(forms.ModelForm):
    class Meta:
        model = ApplicationKZ
        fields = ['name_surname', 'phone_number', 'town']
        widgets = {
            'name_surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя Фамилия'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Номер телефона'}),
            'town': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Город'}),
        }

        error_messages = {
            'name_surname': {
                'required': 'Обязательное поле',
            },
            'phone_number': {
                'required': 'Обязательное поле',
            },
            'town': {
                'required': 'Обязательное поле',
            },
        }

    def __init__(self, *args, **kwargs):
        super(ApplicationFormKZ, self).__init__(*args, **kwargs)
        self.fields['name_surname'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['town'].widget.attrs.update({'class': 'form-control'})

    def is_valid(self):
        for field in self.errors:
            self[field].field.widget.attrs.update({'class': 'form-control is-invalid'})
        return super(ApplicationFormKZ, self).is_valid()
