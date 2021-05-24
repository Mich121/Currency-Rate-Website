from django.shortcuts import render
from django.views import generic
from .models import Post, Comment
from .forms import PostForm, EditPostForm, CommentForm
from django.urls import reverse_lazy

# Create your views here.
class Articles(generic.ListView):
    model = Post
    template_name = 'articles.html'
    ordering = ['-post_date']

class Article(generic.DetailView):
    model = Post
    template_name = 'article.html'

class AddPostView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class UpdatePostView(generic.UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'update_post.html'

class DeletePostView(generic.DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class AddCommentView(generic.CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    success_url = reverse_lazy('home')