from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Article


class blogView(ListView):
    model = Article
    template_name = 'blog/blog.html'


class blog_post_view(DetailView):
    model = Article
    template_name = 'blog/blog_post.html'


class new_post_view(CreateView):
    model = Article
    template_name = 'blog/new_post.html'
    fields = '__all__'


class update_post(UpdateView):
    model = Article
    template_name = 'blog/update_blog.html'
    fields = '__all__'


class delete_post(DeleteView):
    model = Article
    template_name = 'blog/delete_blog.html'
    success_url = reverse_lazy('renureads')