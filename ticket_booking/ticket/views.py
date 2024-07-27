from django.shortcuts import render, redirect, get_object_or_404

from .forms import TicketForm
from .models import TicketBook


def add_ticket(request):
    template_name = 'ticket/add.html'
    form = TicketForm()
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)

def show_ticket(request):
    template_name = 'ticket/show.html'
    tickets = TicketBook.objects.all()
    context = {'tickets': tickets}
    return render(request, template_name, context)


def update_ticket(request, pk):
    obj = TicketBook.objects.get(id=pk)
    form = TicketForm(instance=obj)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    return render(request, template_name='ticket/add.html', context={'form': form})


def cancel_ticket(request, pk):
    obj = TicketBook.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    return render(request, 'ticket/confirm.html')







