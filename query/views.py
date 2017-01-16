from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import QueryForm


def index(request):
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/query/')
    else:
        form = QueryForm()

    return render(request, 'query/index.html', {'form': form})
