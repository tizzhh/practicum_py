from typing import Any

from contest.models import Contest
from django.views.generic import TemplateView


class Description(TemplateView):
    template_name = 'about/description.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['number_of_entries'] = Contest.objects.count()
        return context
