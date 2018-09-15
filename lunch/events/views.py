from django.views.generic import CreateView, DetailView
from .forms import EventForm
from .models import Event

class EventCreateView(CreateView):
    form_class = EventForm
    model = Event

class EventDetailView(DetailView):
    model = Event