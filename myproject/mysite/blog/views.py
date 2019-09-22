from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    objects = Post.objects.all()
    template = 'blog/post_list.html'
    context = {
        'post_list': objects
    }

    return render(request, template, context)

