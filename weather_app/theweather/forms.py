from django.forms import ModelForm, TextInput
from . import models


class CityForm(ModelForm):
    class Meta:
        model = models.City
        fields = ['name', ]
        widgets = {'name': TextInput(attrs={'placeholder': 'City name', 'class': 'input'})}
