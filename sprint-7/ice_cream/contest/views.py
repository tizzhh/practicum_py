from django.shortcuts import render
from .forms import ContestForm


def proposal_create(request):
    return render(request, 'contest/form.html', context={'form': ContestForm()})


def accepted(request):
    return render(request, 'contest/proposal_accepted.html')