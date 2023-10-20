from django.shortcuts import render
from django.http import HttpResponse
from . import models



def postListView(request):
    post_value = models.Post.objects.all()
    return render(request, 'post/post.html', {'post_key': post_value})












def helloView(request):
    return HttpResponse("<h1>Hello! Its my project</h1>")
def now_dateView(request):
    return HttpResponse("<h1>17.10.23</h1>")
def goodbye(request):
    return HttpResponse("<h1>Goodbye user!</h1>")


