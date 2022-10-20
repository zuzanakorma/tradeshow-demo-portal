from django.views.generic import ListView
from .models import Card
from django.conf import settings

class StartingPageView(ListView):
    template_name = "cards/index.html"
    model = Card

    context_object_name = "cards"


    def get_context_data(self, **kwargs):
        context = super(StartingPageView, self).get_context_data(**kwargs)
        context['logo']= settings.LOGO

        return context


