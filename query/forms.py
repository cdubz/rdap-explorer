"""
Forms for the rdap_explorer project, query app.
"""

from django import forms


class QueryForm(forms.Form):
    query = forms.CharField(
        label='',
        max_length=45,  # Max length of an IPv6 address.
        widget=forms.TextInput(attrs={
            'autofocus': 'autofocus',
            'class': 'form-input input-lg',  # TODO: Move this in theme!
            'placeholder': 'IPv4/6 address'
        })
    )
