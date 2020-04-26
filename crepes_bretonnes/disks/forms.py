from django import forms


class SearchForm(forms.Form):
    sujet = forms.CharField(max_length=100, required=False)

