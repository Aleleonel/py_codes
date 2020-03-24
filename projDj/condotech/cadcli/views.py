from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import LoginForm


def get_name(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
