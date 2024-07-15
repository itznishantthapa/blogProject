from django.shortcuts import render,redirect
from blogApp.models import Blog

# Create your views here.
def blog_list(request):
    blogs=Blog.objects.all()
    return render(request, 'blog/blog_list.html',{'blogs':blogs})

def blog_create(request):
    if request.method=="POST":
        title=request.POST['title']
        author=request.POST['author']
        description=request.POST['description']
        Blog.objects.create(title=title,author=author,description=description)
        print("Added successful")
        return redirect('blog_list')
    return render(request, 'blog/blog_create.html')






def blog_edit(request,pk):
    blog=Blog.objects.get(id=pk)
    if request.method=='POST':
        blog.title=request.POST['title']
        blog.description=request.POST['description']
        blog.save()
        return redirect('blog_list')
    return render(request,'blog/blog_edit.html',{'blog':blog})