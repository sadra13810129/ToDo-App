from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from .models import ToDo
from django.views import View
from django.views.generic import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .forms import ToDoEditForm
from django.shortcuts import get_object_or_404

class TaskListView(LoginRequiredMixin,ListView):
    model = ToDo
    context_object_name = 'tasks'
    ordering = '-id'
    template_name = "todo/tasks_list.html"
    def get_queryset(self):
        return self.model.objects.filter(user = self.request.user)
    

class TaskCreateView(LoginRequiredMixin,CreateView):
    model = ToDo
    fields = ["title"]
    success_url = reverse_lazy('todo:task-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect('todo:task-list')
    

class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = ToDo
    form_class = ToDoEditForm
    template_name = 'todo/task_edit.html'
    context_object_name = 'task'
    success_url = reverse_lazy('todo:task-list')

    def get_object(self, queryset=None):
        return get_object_or_404(ToDo, pk=self.kwargs['pk'])



class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model = ToDo
    template_name = 'todo/task_confirm_delete.html'
    success_url = reverse_lazy('todo:task-list')

class TaskDoneOrUnDone(LoginRequiredMixin,View):
    model = ToDo
    success_url = reverse_lazy('todo:task-list')

    def get(self, request, *args, **kwargs):
        object = ToDo.objects.get(id=kwargs.get("pk"))
        object.status =  not object.status
        object.save()
        return redirect(self.success_url)