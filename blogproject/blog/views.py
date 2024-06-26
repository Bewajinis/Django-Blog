from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
# from blogproject.blog.models import Article
from .models import Article

class Index(ListView):
    model = Article
    queryset = Article.objects.all().order_by('-date')
    template_name = 'blog/index.html'
    paginate_by = 1


class DetailArticleView(DetailView):
    model = Article
    template_name = 'blog/blog_post.html'