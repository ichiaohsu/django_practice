from django.shortcuts import render, redirect
from .models import Store
from django.http import Http404, HttpResponse
from django.urls import reverse
from .forms import StoreForm

from django.http import HttpResponseForbidden
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from events.forms import EventForm

# Create your views here.
def store_list(request):
    stores = Store.objects.all()
    return render(request, 'stores/store_list.html', {'stores':stores})

def store_detail(request, pk):
    try:
        store = Store.objects.get(pk=pk)
    except Store.DoesNotExist:
        return Http404
    event_form = EventForm(initial={'store': store}, submit_title='建立活動')
    event_form.helper.form_action = reverse('event_create')
    return render(request, 'stores/store_detail.html', {'store':store, 'event_form':event_form})

def store_create(request):
    if request.method == 'POST':
        form = StoreForm(request.POST, submit_title='建立')
        if form.is_valid():
            store = form.save(commit=False)
            if request.user.is_authenticated:
                store.owner = request.user
            store.save()
            return redirect(store.get_absolute_url())
    else:
        form = StoreForm(submit_title='建立')
    return render(request, 'stores/store_create.html', {'form': form})

def store_update(request, pk):
    try:
        store = Store.objects.get(pk=pk)
    except Store.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        form = StoreForm(request.POST, instance=store, submit_title='更新')
        if form.is_valid():
            store = form.save()
            return redirect(store.get_absolute_url())
    else:
        form = StoreForm(instance=store, submit_title='更新')
    return render(request, 'stores/store_update.html', {
        'form': form, 'store': store,
    })

@login_required
@require_http_methods(['POST', 'DELETE'])
def store_delete(request, pk):
    try:
        store = Store.objects.get(pk=pk)
    except Store.DoesNotExist:
        raise Http404
    if store.can_user_delete(request.user):
        store.delete()
        if request.is_ajax():
            return HttpResponse()
        return redirect('store_list')
    return HttpResponseForbidden()