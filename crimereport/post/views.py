from django.shortcuts import render, redirect
from django.views.generic import ListView,TemplateView
from .models import Post, Comment
from django.core.paginator import Paginator
import json
from django.forms.models import model_to_dict
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.contrib import messages
# Create your views here.

def fn_pagination(request, model, paginate_by = 12):
    paginator = Paginator(model, paginate_by)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj

def postList(request):
    if 'search_text' in request.GET:
        search = request.GET['search_text']
        orders = request.GET['search_order']
        if orders == 'text':
            model = Post.objects.filter(text__contains=search)
        elif orders == 'title':
            model = Post.objects.filter(title__contains=search)
        else:
            model = Post.objects.filter(text__contains=search, title__contains=search)
        page_obj = fn_pagination(request, model)
    elif 'party' in request.GET:
        search = request.GET['party']
        model = Post.objects.filter(title__contains=search)
        page_obj = fn_pagination(request, model)
    else:
        model = Post.objects.all()
        page_obj = fn_pagination(request, model)
    return render(request, 'post/postList.html', {'page_obj':page_obj})


def detailPost(request, post_id):
    detail_post = Post.objects.get(id = post_id)
    comments = Comment.objects.filter(post = post_id).order_by('created')
    context = {'detail_post':detail_post, 'comments':comments}
    return render(request, 'post/detailPost.html', context)

def input_comment(request):
    input_data = request.POST['text']
    post_id = request.POST['post_id']
    Comment.objects.create(
        post = post_id,
        author = 0,
        text = input_data
    )
    comments = model_to_dict(Comment.objects.filter(post= post_id).orderby('created')[-1])
    to_json = {**comments}
    return JsonResponse(to_json)

