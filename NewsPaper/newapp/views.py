from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from django.shortcuts import get_object_or_404

from .models import *

class PostList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'post_list.html'
    context_object_name = 'Posts'
    paginate_by = 10

class AuthorList(ListView):
    model = Author
    context_object_name = 'Authors'
    templates_name = 'newapp/authors.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'newapp/post_detail.html'
    context_object_name = 'Post'
