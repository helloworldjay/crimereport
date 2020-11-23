from django.shortcuts import render, redirect
from django.contrib import auth
from django.views.generic import ListView,TemplateView
from .models import Post, Comment
from django.core.paginator import Paginator
import json
from django.forms.models import model_to_dict
from django.http.response import JsonResponse
from .forms import CommentForm
# Create your views here.

def fn_pagination(request, model, paginate_by = 12):
    paginator = Paginator(model, paginate_by)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj

def postlist(request):
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


def detailpost(request, post_id):
    comment_form = CommentForm(request.POST)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        comment_form.instance.post= Post.objects.get(id = post_id)
        comment_form.instance.author = auth.get_user(request)
        if comment_form.is_valid():
            create_comment = comment_form.save()
            return redirect(detailpost, post_id)
    else:
        detail_post = Post.objects.get(id = post_id)
        # comments = Comment.objects.select_related('post').filter(id = post_id).order_by('created')
        comments = detail_post.comments.all()
        context = {'detail_post':detail_post, 'comments':comments,'comment_form':comment_form}
        return render(request, 'post/detailPost.html', context)

def input_comment(request, post_id):
    # if request.method == 'POST':
    #     comment_form = CommentForm(request.POST)
    #     comment_form.instance.post = post_id
    #     comment_form.instance.author = request.user.id
    #     if comment_form.is_valid():
    #         create_comment = comment_form.save()
        return redirect(detailpost)
    # comments = model_to_dict(Comment.objects.filter(post= post_id).orderby('created')[-1])
    # to_json = {**comments}
    # return JsonResponse(to_json)
