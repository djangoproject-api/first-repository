from django.shortcuts import render,get_object_or_404
from .models import Post

from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.
def post_list_view(request):
    post_list=Post.objects.all()
    paginator=Paginator(post_list,1)
    page_number=request.GET.get('page')
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,'app1/post_list.html',{'post_list':post_list})

from django.views.generic import ListView
class postlistview(ListView):
    paginate_by = 1
    model=Post



def post_detail_view(request,post,year,month,day):
    post=get_object_or_404(Post,slug=post,
                           status='published',
                           publish__year=year,
                           publish__month=month,
                           publish__day=day)

    return render(request,'app1/post_detail.html',{'post':post})