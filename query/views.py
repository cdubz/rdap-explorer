"""
Views for the rdap_explorer project, query app.
"""

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from ipwhois import IPWhois
from json import dumps

from .forms import QueryForm


def index(request):
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse(
                'query:results',
                args=(form['query'].value(),)
            ))
    else:
        form = QueryForm()

    return render(request, 'query/index.html', {
        'title': 'Query',
        'form': form
    })


def results(request, query):
    form = QueryForm(initial={"query": query})
    ip = IPWhois(query)
    results = ip.lookup_rdap(retry_count=1, depth=2, inc_raw=True)
    return render(request, 'query/index.html', {
        'title': 'Results',
        'form': form,
        'results': dumps(results)
    })
