from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect

from blog.forms import PostCommentForm
from blog.models import *
from shop.models import *
from shop.forms import ProductForm


def home_view(request):
    categories = PostCategory.objects.all()
    posts = Post.objects.all().order_by('-created_at')
    products = Product.objects.all().order_by('-created_at')

    context = {
        'categories': categories,
        'posts': posts,
        'products': products,
    }

    return render(request, 'home.html', context)


def blog_list(request):
    posts = Post.objects.all().order_by('-created_at')
    categories = PostCategory.objects.all().order_by('title')
    tags = PostTag.objects.all().order_by('title')

    context = {
        'posts': posts,
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'blog/blog.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()

    if request.method == 'POST':
        if 'add_comment' in request.POST:
            comment_form = PostCommentForm(request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.post = post
                new_comment.author = request.user
                new_comment.save()
                return redirect('blog:post_detail', pk=post.pk)
    else:
        comment_form = PostCommentForm()

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'blog/post_detail.html', context)


@login_required
def delete_post_comment(request, comment_id):
    comment = get_object_or_404(PostComment, id=comment_id)
    if request.user == comment.author or request.user.is_superuser:
        if request.method == 'POST':
            post_id = comment.post.id
            comment.delete()
            return redirect('blog:post_detail', pk=post_id)
        return redirect('blog:post_detail', pk=comment.post.id)
    else:
        return  HttpResponseForbidden("У вас нет прав для удаления этого комментария.")

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

handler404 = custom_404_view