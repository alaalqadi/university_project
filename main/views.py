from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from main.models import Post
from . import forms
from . import models
import logging

from django.contrib.auth.decorators import login_required
logger = logging.getLogger('django')


# Create your views here.
@login_required()
def index(request):
    posts = Post.objects.filter(status=Post.STATUS_OPEN)

    return render(request, 'main/index.html', locals())


def add_edit_post(request, id=None):
    post = Post()
    form = forms.PostForm(request.POST or None, request.FILES or None, instance=post)
    if id:
        post = get_object_or_404(Post, pk=id)
        initial = {
            'description': post.description,
            'name': post.name,
            'attachment': post.attachment
        }

        form = forms.PostForm(request.POST or None, request.FILES or None, instance=post, initial=initial)

    if form.is_valid():
        post.status = Post.STATUS_OPEN
        post.user = request.user
        form.save()

        return HttpResponseRedirect(reverse('home'))

    return render(request, 'main/add_post.html', locals())


def delete_post(request, id=None):
    post = Post.objects.get(id=id)
    post.status = Post.STATUS_DELETED
    post.save()
    return HttpResponseRedirect(reverse('home'))
