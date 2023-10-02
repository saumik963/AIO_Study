from django import forms
from django.forms import widgets
from Study.models import Notes


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['Title', 'Description']


class search(forms.Form):
    text = forms.CharField(max_length=100, label="Search here", required=False)


class cal(forms.Form):
    num = forms.IntegerField()


class Mod(forms.Form):
    num = forms.IntegerField()
    mod = forms.IntegerField()
