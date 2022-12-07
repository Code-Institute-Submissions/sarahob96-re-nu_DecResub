from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article


class blogView(ListView):
    model = Article
    template_name = 'blog/blog.html'

