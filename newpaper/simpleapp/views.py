from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from news.models import Post, Category
from django.core.paginator import Paginator
from .filters import NewFilter
from simpleapp.forms import NewForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin

class NewList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    ordering = ['-datepost']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewFilter(self.request.GET,queryset=self.get_queryset())
        return context

class NewDetailView(DetailView):
    template_name = 'new_detail.html'
    queryset = Post.objects.all()
    context_object_name = 'news'

class NewsSearch(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewFilter(self.request.GET,queryset=self.get_queryset())
        return context
    
class NewUpdateView(PermissionRequiredMixin, CreateView):
    template_name = 'new_create.html'
    permission_required = ('news.change_post',)
    form_class = NewForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)
    
class NewDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'new_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
    context_object_name = 'news'

class MyView(PermissionRequiredMixin, View):
    permission_required = ('<app>.<action>_<model>',
                           '<app>.<action>_<model>')

class AddPost(PermissionRequiredMixin, CreateView):
    queryset = Post.objects.all()
    template_name = 'new_create.html'
    permission_required = ('news.add_post',)
    form_class = NewForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewFilter(self.request.GET, queryset=self.get_queryset())
        context['form'] = NewForm()
        return context















