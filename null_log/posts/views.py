from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def inicio(request):
    post = Post.object.all().orde_by('fecha_creacion')
    return render(request, 'inicio.html', {'posts': posts})

def detale_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'detalle_post.html', {'post': post})
