from django.conf import settings
from django.urls import reverse
from django.db import models

from stores.models import MenuItem


class Event(models.Model):

    store = models.ForeignKey('stores.Store', related_name='events', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.store)

    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'pk': self.pk})


class Order(models.Model):

    event = models.ForeignKey(Event, related_name='orders', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='orders', on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, related_name='orders', on_delete=models.CASCADE)
    notes = models.TextField(blank=True, default='')

    class Meta:
        unique_together = ('event', 'user',)

    def __str__(self):
        return '{item} of {user} for {event}'.format(
            item=self.item, user=self.user, event=self.event
        )