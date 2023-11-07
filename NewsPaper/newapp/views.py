from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


from .filters import PostFilter
from .forms import PostForm
from .models import *

@login_required
def show_protected_page(request):
    pass

class PostList(ListView):
    model = Post
    ordering = 'dateCreation'
    template_name = 'post_list.html'
    context_object_name = 'Posts'
    paginate_by = 10


class PostSearch(ListView):
    model = Post
    template_name = 'post_list'
    context_object_name = 'Posts'
    filterset_class = PostFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class AuthorList(ListView):
    model = Author
    context_object_name = 'Authors'
    templates_name = 'newapp/authors.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'newapp/post_detail.html'
    context_object_name = 'Post'

class PostCreate(PermissionRequiredMixin, UpdateView, LoginRequiredMixin, CreateView):
    permission_required = ('newapp.add_Post',)
    form_class = PostForm
    model = Post
    template_name = 'newapp/post_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'NW'
        return super().form_valid(form)

    def add_post(request):
        if not request.user.has_perm('newapp.add_post'):
            raise PermissionDenied

class ArticleCreate(PermissionRequiredMixin, UpdateView, LoginRequiredMixin, CreateView):
    permission_required = ('newapp.add_Post',)
    form_class = PostForm
    model = Post
    template_name = 'newapp/article_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'AR'
        return super().form_valid(form)

class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('newapp.delete_Post',)
    model = Post
    template_name = 'newapp/post_delete.html'
    success_url = reverse_lazy('post_list')

class PostEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('newapp.change_Post',)
    model = Post
    form_class = PostForm
    template_name = 'newapp/post_edit.html'

class ArticleDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('newapp.delete_Post',)
    model = Post
    template_name = 'newapp/article_delete.html'
    success_url = reverse_lazy('article_list')

class ArticleEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('newapp.change_Post',)
    form_class = PostForm
    model = Post
    template_name = 'newapp/article_edit.html'

class AuthorCreateView(CreateView):
    model = Author
    fields = ['name']
    template_name = 'author_form.html'