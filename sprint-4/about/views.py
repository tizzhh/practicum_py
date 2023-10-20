from django.http import HttpResponse

from django.shortcuts import render


def description(request):
    template_name = 'about/description.html'

    return render(request, template_name)