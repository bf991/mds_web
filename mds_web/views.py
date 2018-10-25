from django.shortcuts import render, get_object_or_404
from news.models import News
from masterclass.models import Masterclass, Masterclass_events

from django.shortcuts import render
from django.views.generic.list import ListView

class MK_eventsListView(ListView):
    model = Masterclass_events
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(MK_eventsListView, self).get_context_data(*args, **kwargs)
        context['masterclass_events'] = self.model.objects.all()
        return context