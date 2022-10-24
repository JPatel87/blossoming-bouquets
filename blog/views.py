from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post, Comment


from .forms import AddPostForm
from .forms import CommentForm


# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

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

    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})


@login_required(login_url="/accounts/login/")
def add_post(request):

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


@login_required(login_url="/accounts/login/")
def edit_post(request, slug):

    """
    Function to view edit services page.

    The get request returns the edit services page.
    The post request checks the form is valid,
    saves the form if valid,
    returns services page and displays
    the success message. If not valid, error message
    is displayed.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('blog'))

    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your post has been edited')
            return redirect(reverse('post_detail', kwargs={'slug': slug}))

    form = AddPostForm(instance=post)

    context = {
        'post': post,
        'form': form
    }
    return render(request, 'blog/edit_post.html', context)


@login_required(login_url="/accounts/login/")
def delete_post(request, slug):

    """
    Function to view edit services page.

    The get request returns the edit services page.
    The post request checks the form is valid,
    saves the form if valid,
    returns services page and displays
    the success message. If not valid, error message
    is displayed.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('blog'))
        
    post = Post.objects.get(slug=slug)

    if request.method == "POST":
        post.delete()
        messages.success(request, 'Your post has been deleted')
        return redirect(reverse('blog'))

    context = {
        'post': post,
        'slug': slug
    }

    return render(request, 'blog/delete_post.html', context)


@login_required(login_url="/accounts/login/")
def edit_comment(request, comment_id, slug):
    """
    Function to view to edit a comment.

    The get request returns the post_detail page with the comment instance.
    The post request edits the comment instance.
    """
    post = Post.objects.get(slug=slug)
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

    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})


@login_required(login_url="/accounts/login/")
def delete_comment(request, comment_id, slug):
    """
    Function to view to delete a comment.

    The get request returns the delete comments page.
    The post request deletes the comment instance.
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
