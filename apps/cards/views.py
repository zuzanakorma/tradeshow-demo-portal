from django.conf import settings
from django.views.generic import ListView

from .models import Card


class StartingPageView(ListView):
    template_name = "cards/index.html"
    model = Card
    context_object_name = "cards"

    def get_context_data(self, **kwargs):
        context = super(StartingPageView, self).get_context_data(**kwargs)
        context['logo'] = settings.LOGO

        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            search_results = Card.objects.search(query)
            qs = sorted(search_results,
                        key=lambda instance: instance.pk,
                        reverse=True)
            return qs
        return Card.objects.filter(visible=True).order_by('title')
