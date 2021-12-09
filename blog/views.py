from django.shortcuts import render

from django.http import HttpResponse

from blog.models import Posts, Coment

# Create your views here.
def name(request):
    return HttpResponse("HttpResponse")

def get_real_posts(request):
    context = {
        'posts': Posts.objects.all()

    }
    return render(request, 'post_list.html', context)

def get_comment(request):
     file = {
         'comment': Coment.objects.all()

     }
     return  render(request, 'comment_list.html', file)
