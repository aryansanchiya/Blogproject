from django.core import paginator
from django.http.response import HttpResponse 
from django.shortcuts import render,get_object_or_404
from. models import blogdetail,Comment,Projects
from.forms import CommentForm
from django.core.paginator import EmptyPage, InvalidPage, Paginator

# Create your views here.

def index(request):
    blogs = blogdetail.objects.all().order_by('-date')
    print(blogs) 
    return render(request,"index.html",{'blogs':blogs})

def about(request): 
    return render(request,'about.html')

def post(request,id):
    table = Comment.objects.all().filter(post=id)
    # post = get_object_or_404(blogdetail, id=id)
    blog = blogdetail.objects.get(id=id)
    # comments = blog.comment.filter(active=True)
    new_comment = None
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = blog
            new_comment.save()
            # print(Comment.post)
            table = Comment.objects.all().filter(post=id)
            print(table)
            print(table)
            return render(request,'post.html',{'table':table,'new_comment':new_comment,'form':form,'blog':blog})
        else:
            return HttpResponse("Doesn't work ")
    return render(request,'post.html',{'blog':blog,'form':form,'new_comment':new_comment,'table':table})

def contact(request):
    return render(request,'contact.html')

def blog(request):
    older_blog = blogdetail.objects.all().order_by('date')
    paginator =Paginator(older_blog,4)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(request,'blog.html',{'older_blog':page_obj})

def projects(request):
    projects = Projects.objects.all()
    return render(request, "projects.html",{'projects':projects})