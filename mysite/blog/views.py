from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Post
from django.http import Http404
from django.shortcuts import get_object_or_404
# Create your views here.

def post_list(request: HttpRequest) -> HttpResponse:
    '''
    Get all post
    '''
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request: HttpRequest, id: int) -> HttpResponse:
    '''
    Get post by id
    '''
    # try:
    #     post = Post.published.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404("Post does not exist")
    
    # using shortcut
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    
    return render(request, 'blog/post/detail.html', {'post': post})