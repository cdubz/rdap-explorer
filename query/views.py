"""
Views for the rdap_explorer project, query app.
"""

import ipwhois
import warnings

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from json import dumps
from pycountry import countries

from .forms import QueryForm
from .models import Log


def index(request):
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            log = Log(query=form['query'].value(),
                      private=form['private'].value())
            log.save()
            return HttpResponseRedirect(reverse(
                'query:results',
                args=(form['query'].value(),)
            ))
    else:
        form = QueryForm()

    return render(request, 'query/index.html', {
        'title': 'Query',
        'form': form,
        'recent_queries': Log.objects.filter(
            private=False
        ).order_by('-date')[:6],
    })


@cache_page(86400)
@csrf_protect
def results(request, query):
    error = None
    result = {}
    form = QueryForm(initial={"query": query})

    country = None
    roles = {}
    try:
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=UserWarning)
            ip = ipwhois.IPWhois(query)
            result = ip.lookup_rdap(retry_count=1, depth=2)

        if result['asn_country_code']:
            country = countries.get(
                alpha_2=result['asn_country_code']).name

        for object_name in result['objects']:
            contact = result['objects'][object_name]['contact']
            for role in result['objects'][object_name]['roles']:
                if role not in roles:
                    roles[role] = {}
                    if contact['name'] is not None:
                        roles[role]['name'] = contact['name']
                    if contact['email'] is not None:
                        roles[role]['email'] = contact['email'][0][
                            'value']
    except (ValueError, ipwhois.exceptions.IPDefinedError) as e:
        error = e

    return render(request, 'query/index.html', {
        'country': country,
        'error': error,
        'form': form,
        'roles': roles,
        'result': dumps(result),
        'title': query,
        'recent_queries': Log.objects.filter(
            private=False
        ).order_by('-date')[:6],
    })
