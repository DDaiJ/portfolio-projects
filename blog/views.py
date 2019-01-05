from django.shortcuts import render, get_object_or_404 #get detailed blog page if exists and 404 if not
from .models import Blog

# Create your views here.
def allblogs(request):
    allblogs = Blog.objects.order_by('-pub_date') #biggest date first = newest, hence - sign
    return render(request, 'blog/allblogs.html', {'allblogs' : allblogs})

def detail(request, blog_id):
    blogdetail = get_object_or_404(Blog, pk=blog_id) #pk: primary key
    return render(request, 'blog/detail.html', {'blog':blogdetail})
