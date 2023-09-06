from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.shortcuts import get_object_or_404

from .filters import PostFilter
from .forms import PostForm
from .models import *

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

class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'newapp/post_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'NW'
        return super().form_valid(form)

class ArticleCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'newapp/article_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'AR'
        return super().form_valid(form)

class PostDelete(DeleteView):
    model = Post
    template_name = 'newapp/post_delete.html'
    permission_required = ('news.delete_post')
    success_url = reverse_lazy('post_list')

class PostEdit(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'newapp/post_edit.html'

class ArticleDelete(DeleteView):
    model = Post
    permission_required = ('news.delete_post')
    template_name = 'newapp/article_delete.html'
    success_url = reverse_lazy('article_list')

class ArticleEdit(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'newapp/article_edit.html'

class AuthorCreateView(CreateView):
    model = Author
    fields = ['name']
    template_name = 'author_form.html'