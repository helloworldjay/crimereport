from django.shortcuts import render
from django.views.generic import ListView,TemplateView
from .models import Post
# Create your views here.


# def postList(request):
#     return render(request, 'post/postList.html', {})

class PostList(ListView):
    paginate_by = 2
    model = Post
    template_name= 'post/postList.html'
    
