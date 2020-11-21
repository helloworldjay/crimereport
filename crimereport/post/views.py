from django.shortcuts import render
from django.views.generic import ListView,TemplateView
from .models import Post
from django.core.paginator import Paginator
# Create your views here.


# def postList(request):
#     return render(request, 'post/postList.html', {})

# class PostList(ListView):
#     paginate_by = 12
#     model = Post
#     template_name= 'post/postList.html'

#     def get(self, request):
#         paginator = Paginator(self.model, self.paginate_by)
#         page_number = request.GET.get('page')
#         page_obj = paginator.get_page(page_number)
#         if 'search_text' in request.GET:
#             search = request.GET['search_text']
#             self.model = Post.objects.filter(title__contains=search)
#             paginator = Paginator(self.model,self.paginate_by)

#             page_number = request.GET.get('page')
#             page_obj = paginator.get_page(page_number)
#             return render(request, 'post/postList.html', {'page_obj':page_obj})
#         return render(request, 'post/postList.html', {'page_obj':page_obj})
def fn_pagination(request, model, paginate_by = 12):
    paginator = Paginator(model, paginate_by)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj

def postList(request):
    if 'search_text' in request.GET:
        search = request.GET['search_text']
        model = Post.objects.filter(text__contains=search)
        page_obj = fn_pagination(request, model)
    elif 'party' in request.GET:
        search = request.GET['party']
        model = Post.objects.filter(text__contains=search)
        page_obj = fn_pagination(request, model)
    else:
        model = Post.objects.all()
        page_obj = fn_pagination(request, model)
    return render(request, 'post/postList.html', {'page_obj':page_obj})


def detailPost(request, post_id):
    detail_post = Post.objects.filter(id = post_id)
    context = {'detail_post':detail_post}
    return render(request, 'post/detailPost.html', context)