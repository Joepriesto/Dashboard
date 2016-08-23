from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import HttpResponseRedirect
from datetime import datetime
from django.urls import reverse
from django.views import generic

# Create your views here.
from .models import Batch, runPeriod


class IndexView(generic.ListView):
    template_name = 'timer/index.html'
    context_object_name = 'latest_lot_list'

    def get_queryset(self):
        """Return the last five Lots"""
        return Batch.objects.order_by('-start_date')[:5]


class DetailView(generic.DetailView):
    model = Batch
    template_name = 'timer/detail.html'


class RunningView(generic.DetailView):
    model = Batch
    template_name = 'timer/running.html'


"""def index(request):
    latest_lot_list = Batch.objects.order_by('-start_date')[:5]
    context = {'latest_lot_list': latest_lot_list}
    return render(request, 'timer/index.html', context)

def detail(request, lot_number):
    batch = get_object_or_404(Batch, lot_number=lot_number)
    context = {'batch.id': batch.lot_number}
    return render(request, 'timer/detail.html', context)"""


def start(request, lot_number):
    batch = get_object_or_404(Batch, lot_number=lot_number)
    run = runPeriod(start_time=datetime.now(), batch=batch)
    return HttpResponseRedirect(reverse('timer:running', args=(batch.lot_number,)))

"""def running(request, lot_number):
    batch = get_object_or_404(Batch, lot_number=lot_number)
    return render(request, 'polls/results.html', {'batch.id':batch.lot_number})
"""
