# from django.shortcuts import render, get_object_or_404
from django.views import generic
# from django import views
# from django.http import HttpResponse

from .forms import CatForm
from .models import Cat

PATH_TO_CRUD = 'crud.html'
REDIRECT_URL = '/read'


# class ReadCatView(views.View):
#
#     cf = CatForm()
#
#     def get(self, *args, **kwargs):
#         return render(self.request, PATH_TO_CRUD, {'form': self.cf})
#
#     def post(self, *args, **kwargs):
#         return HttpResponse('<h1>method: post</h1>')
#
#
# class CreateCatView(generic):
#
#     def get(self, *args, **kwargs):
#         Cat.objects.create(name=self.request.GET.get('name'), age=self.request.GET.get('age'))
#
#
# class DeleteCatView(generic):
#     pass
#
#
# class UpdateCatView(generic):
#     pass
#
#
# class DetailCatView(views.View):
#
#     def get(self, request, pk, *args, **kwargs):
#         task: Cat = get_object_or_404(Cat, pk=pk)
#         return HttpResponse(f'{task.name}: {task.is_status}')

class ReadCatView(generic.ListView):
    model = Cat
    template_name = PATH_TO_CRUD
    context_object_name = 'cats'


class CreateCatView(generic.CreateView):
    model = Cat
    form_class = CatForm
    template_name = PATH_TO_CRUD
    success_url = REDIRECT_URL


class DeleteCatView(generic.DeleteView):
    model = Cat
    template_name = PATH_TO_CRUD
    success_url = REDIRECT_URL
    # context_object_name = 'delete'


class UpdateCatView(generic.UpdateView):
    model = Cat
    form_class = CatForm
    template_name = PATH_TO_CRUD
    success_url = REDIRECT_URL


class DetailCatView(generic.DetailView):
    model = Cat
    template_name = PATH_TO_CRUD
    context_object_name = 'cat'
