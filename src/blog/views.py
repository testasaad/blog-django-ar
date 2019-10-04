from django.shortcuts import render, get_object_or_404

from .models import Post, Comment
# Create your views here.
from .forms import NewCommentForm


def home(request):
    context = {
        'title':'الصفحة الرئيسية',
        'posts':Post.objects.all(),

    }
    return render(request, 'blog/index.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'من انا'})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.filter(active=True)
    comment_form = NewCommentForm()
    new_comment = None
    context = {
        'title': post,
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }

    if request.method == 'POST':
        comment_form = NewCommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            comment_form = NewCommentForm()
    else:
        comment_form = NewCommentForm()
    return render(request, 'blog/detail.html', context)