from django.shortcuts import render, get_object_or_404
from  .models import Blog

def all_blogs(request):
    allBlogs = Blog.objects.order_by('-date')[:5]
    return render(request, 'blog/blogs.html', {'allBlogs': allBlogs})

def blogDetail(request, blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    return render(request, 'blog/blogDetail.html', {'blog' : blog})
