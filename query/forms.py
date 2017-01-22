"""
Forms for the rdap_explorer project, query app.
"""

from django import forms


class QueryForm(forms.Form):
    query = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'IPv4/6 address'})
    )
