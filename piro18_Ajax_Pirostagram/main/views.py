from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from .models import Comment, Like

# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    ctx = {
        'posts': posts,
    }
    return render(request, 'main/post_list.html', ctx)


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:post_list')
        else:
            ctx = {
                'form': form,
            }
            return render(request, 'main/post_new.html', ctx)
    elif request.method == 'GET':
        form = PostForm()
        ctx = {
            'form': form,
        }
        return render(request, 'main/post_new.html', ctx)
    
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def like_ajax(request):
    req = json.loads(request.body)
    post_id = req ['id']
    button_type = req ['type']
    
    post = Post.objects.get(id=post_id)
    
    if button_type == 'like':
        post.like += 1
        
    post.save()
    return JsonResponse({'id': post_id, 'type': button_type})


@csrf_exempt
def create_comment(request, *args, **kwargs):
  req = json.loads(request.body)
  text = req['text']  
  newComment = Comment(comment = text)
  newComment.save()
  return JsonResponse({'id': newComment.pk, 'text': newComment.comment})

@csrf_exempt
def delete_comment(request, *args, **kwargs):
  req = json.loads(request.body)
  id = req['id']
  Comment.objects.all().get(id=id).delete()
  return JsonResponse({'id': id})
