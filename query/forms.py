from django import forms


class QueryForm(forms.Form):
    query = forms.CharField(max_length=100)
