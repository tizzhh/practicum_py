from django.shortcuts import render

from .models import Contest
from .forms import ContestForm


def proposal(request):
    form = ContestForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        form.save()
    return render(request, 'contest/form.html', context)


def proposal_list(request):
    contest_list = Contest.objects.all().order_by('id')
    return render(
        request,
        'contest/contest_list.html',
        context={'contest_list': contest_list},
    )
