"""Imports from django and post and comment models and forms."""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import AddPostForm
from .forms import CommentForm


def blog(request):
    """
    View blog overview page.
    """
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})


def post_detail(request, slug):
    """
    View post detail and add comment.

    If comment form is valid, save,
    return the blog post. Else,
    return error message.
    """

    query = Post.objects
    post = get_object_or_404(query, slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.post = post
            instance.save()
            messages.success(request, 'Your comment has been added')

            return redirect('post_detail', slug)
        else:
            messages.error(request, 'Errors on form, not submitted')
    else:
        form = CommentForm()

    return render(
        request,
        'blog/post_detail.html',
        {'post': post, 'form': form}
        )


@login_required
def add_post(request):
    """
    View add post form by admin only.

    If comment form is valid,
    save, return the blog overview page. Else,
    return error message.
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('blog'))

    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, 'Post has been created')

            return redirect('blog')
        else:
            messages.error(request, 'Errors on form, not submitted')
    else:
        form = AddPostForm()

    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_post(request, slug):
    """
    View edit post form by admin only.

    If comment form is valid,
    save, return the post detail page. Else,
    return error message.
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('blog'))

    query = Post.objects
    post = get_object_or_404(query, slug=slug)

    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your post has been edited')
            return redirect(reverse('post_detail', kwargs={'slug': slug}))
        else:
            messages.error(request, 'Errors on form, not submitted')

    form = AddPostForm(instance=post)

    context = {
        'post': post,
        'form': form
    }
    return render(request, 'blog/edit_post.html', context)


@login_required
def delete_post(request, slug):
    """
    View to delete post by admin only.
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('blog'))

    query = Post.objects
    post = get_object_or_404(query, slug=slug)

    if request.method == "POST":
        post.delete()
        messages.success(request, 'Your post has been deleted')
        return redirect(reverse('blog'))

    context = {
        'post': post,
        'slug': slug
    }

    return render(request, 'blog/delete_post.html', context)


@login_required
def edit_comment(request, comment_id, slug):
    """
    View edit comment form by authenticated users.

    If comment form is valid,
    save, return the post detail page. Else,
    return error message.
    """

    query = Post.objects
    post = get_object_or_404(query, slug=slug)
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your comment has been edited')
            return redirect(reverse('post_detail', kwargs={'slug': slug}))
        else:
            messages.error(request, 'Errors on form, not submitted')

    form = CommentForm(instance=comment)
    messages.info(request, 'You are about to edit your comment')

    return render(
        request,
        'blog/post_detail.html',
        {'post': post, 'form': form}
        )


@login_required
def delete_comment(request, comment_id, slug):
    """
    View to delete comment by authenticated users.
    """

    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == "POST":
        comment.delete()
        messages.success(request, 'Comment has been deleted')
        return redirect(reverse('post_detail', kwargs={'slug': slug}))

    context = {
        'comment': comment,
        'slug': slug
    }
    return render(request, 'blog/delete_comment.html', context)
