"""
Views for the rdap_explorer project, query app.
"""

import ipwhois

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
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


@cache_page(86400)
@csrf_protect
def results(request, query):
    error = None
    result = {}
    form = QueryForm(initial={"query": query})

    try:
        ip = ipwhois.IPWhois(query)
        result = ip.lookup_rdap(retry_count=1, depth=2)
    except (ValueError, ipwhois.exceptions.IPDefinedError) as e:
        error = e

    roles = {}
    for object_name in result['objects']:
        contact = result['objects'][object_name]['contact']
        for role in result['objects'][object_name]['roles']:
            if role not in roles:
                roles[role] = {}
                if contact['name'] is not None:
                    roles[role]['name'] = contact['name']
                if contact['email'] is not None:
                    roles[role]['email'] = contact['email'][0]['value']

    return render(request, 'query/index.html', {
        'title': query,
        'error': error,
        'form': form,
        'roles': roles,
        'result': dumps(result)
    })
