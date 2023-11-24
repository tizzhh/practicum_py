from django.shortcuts import render
from .forms import ContestForm


def proposal(request):
    return render(request, 'contest/form.html', context={'form': ContestForm(request.GET or None)})