"""
Forms for the rdap_explorer project, query app.
"""

from django import forms


class QueryForm(forms.Form):
    query = forms.CharField(max_length=100)
