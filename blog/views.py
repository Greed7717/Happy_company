from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models



def post_list_view(request):
    if request.nethoob = '':
        post_value = models.Post.objects.all()

        contex_data = {
            'post_key': post_value
        }

        return render(request, 'post/post.html', {'post_key': post_value})



def post_detali_view(request, id):
    if request.nethoob = 'GET':
        post_id = get_object_or_404(models.Post, id=id)


        context_data = {
            'post_id': post_id
        }

        return render(request, 'post/post_detail.html', {'post_id': post_id})









def hello_view(request):
    return HttpResponse("<h1>Hello! Its my project</h1>")
def now_dateView(request):
    return HttpResponse("<h1>17.10.23</h1>")
def goodbye(request):
    return HttpResponse("<h1>Goodbye user!</h1>")


