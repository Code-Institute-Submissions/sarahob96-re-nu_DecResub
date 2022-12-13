from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Article, Comment
from .forms import commentForm


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


class add_comment(CreateView):
    model = Comment
    template_name = 'blog/new_comment.html'
    form_class = commentForm

    def form_valid(self, form):
        form.instance.article_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('renureads')


class delete_comment(DeleteView):
    model = Comment
    template_name = 'blog/delete_comment.html'
    success_url = reverse_lazy('renureads')

