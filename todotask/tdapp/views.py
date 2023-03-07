from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView
from .models import task
from .form import tdform
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


class tdlist(ListView):
    model = task
    template_name = 'home.html'
    context_object_name = 'Task1'


class tddetail(DetailView):
    model = task
    template_name = 'details.html'
    context_object_name = 'tsk'


class tdupdate(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'tk'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('detailview', kwargs={'pk': self.object.id})


class tddelete(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('listview')


def home(request):
    Task1 = task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        Task = task(name=name, priority=priority, date=date)
        Task.save()

    return render(request, 'home.html', {'Task1': Task1})


def details(request):
    Task = task.objects.all()
    return render(request, 'details.html')


def delete(request, Taskid):
    Task = task.objects.get(id=Taskid)
    if request.method == "POST":
        Task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
    Task = task.objects.get(id=id)
    frm = tdform(request.POST or None, instance=Task)
    if frm.is_valid():
        frm.save()
        return redirect('/')
    return render(request, 'edit.html', {'frm': frm, 'Task': Task})
