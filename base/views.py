from django.views.generic import ListView
from apps.cards.models import Card


class SearchView(ListView):
    model = Card
    template_name = "cards/search.html"
    count = 0
    # paginate_by= 3

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            search_results = Card.objects.search(query)
            qs = sorted(search_results,
                        key=lambda instance: instance.pk,
                        reverse=True)
            return qs
        return Card.objects.none() # just an empty queryset as default