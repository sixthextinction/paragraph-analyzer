from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import PostForm
from .models import Post


# Create your views here.
def post_list(request):
    list_of_posts = Post.objects.all().order_by("-analyzed_at")
    context = {
        "title": "List of Analyses",
        "list_of_posts": list_of_posts,
    }
    return render(request, "index.html", context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        "title": "Analysis",
        "post": post,
    }
    return render(request, "post_detail.html", context)


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        created_post = form.save()
        created_post.save()
        # redirect to detail page
        return HttpResponseRedirect(Post.get_absolute_url(created_post))

    context = {
        "title": "Form",
        "form": form,
    }

    return render(request, "analysis_form.html", context)
