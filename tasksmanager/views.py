from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout
from django.contrib.auth import login
from .models import Task, Photo, Video
from .forms import TaskForm, PhotoForm
from django.db import transaction
from django.views.generic import CreateView

def view_enter(request):
    if request.user.is_authenticated():
        return redirect('view_task')
    else:
        return render(request, 'Enter.html')


def view_task(request):
    user = request.user
    l = request.user.groups.values_list('name', flat=True)
    l = str(l)
    print(l)
    if l == "<QuerySet ['Students']>":
        if request.user.is_authenticated():
            task = Task.objects.filter(user = user)
            print(task,user)
            return render(request, 'Task.html', {'task': task, 'user': user})

        else:
            return render(request, 'Enter.html')
    else:
        if request.user.is_authenticated():
            task = Task.objects.filter(author=user)
            return render(request, 'Task.html', {'task': task, 'user': user})
        else:
            return render(request, 'Enter.html')


def forms(request):
    user = request.user
    l = request.user.groups.values_list('name', flat=True)
    l = str(l)
    if l != "<QuerySet ['Students']>":
        if request.method == "POST":
            form = TaskForm(request.POST)
            if form.is_valid():
                task = form.save(commit=False)
                task.author = request.user
                task.save()
                return redirect('view_task')
        else:
            form = TaskForm()
        return render(request, 'Form.html', {'form': form, 'user': user})
    else:
        return render(request, 'student.html')


def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()

            return redirect('view_task')
    else:
        form = TaskForm(instance=task)
    return render(request, 'Form.html', {'form': form})


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/view_task"
    template_name = "login.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "auth.html"
    success_url = "/view_task"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/view_enter")