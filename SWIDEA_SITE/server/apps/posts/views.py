from django.shortcuts import render,redirect
from .models import Post
from .forms import idForm

def id_list(request):
    post_list=Post.objects.order_by('name')
    context = {'post_list':post_list}
    return render(request,"posts/id_list.html", context=context)

def id_detail(request,pk,*args, **kwargs):
    post = Post.objects.get(id=pk)
    context={
        "post_id":post,
    }
    return render(request, "posts/id_detail.html", context=context)

def id_create(request):
    ids = Post.objects.all()
    if request.method == "POST":
        form = idForm(request.POST, request.FILES)
        if form.is_valid():
            id= form.save(commit=False)
            id.user = request.user
            id.save()
            return redirect('/')
        else:
            return redirect('/')
    else:
        form = idForm()
        context={
            'form':form,
            'ids':ids,
        }
        return render(request, 'posts/id_create.html',context=context)
            
        #Post.objects.create(
         #   title=request.POST["title"],
          #  devtool=request.POST["devtool"],
           # interest=request.POST["interest"],
            #content=request.POST["content"],
            #image=request.FILES["image"],
        #)
        #return redirect("/")
    #return render(request, "posts/id_create.html")


def id_update(request):
    post_list=Post.objects.order_by('title')
    context={'post_list':post_list}
    return render(request,"posts/id_list.html",context)