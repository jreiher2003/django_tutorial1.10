from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post 

# Create your views here.
def post_create(request):
    return HttpResponse("<h1>Create!</h1>")

def post_detail(request):
    instance = get_object_or_404(Post,title="New Title")
    context = {"title": "Detail Title", "instance": instance}
    return render(request, "post_detail.html", context)

def post_list(request):
    # if request.user.is_authenticated():
    #     context = {"title": "List Title logged in"}
    # else:
    #     context = {"title": "Not logged in"}
    queryset = Post.objects.all()
    context = {"title": "List Title", "queryset": queryset}
    return render(request, "index.html", context)

def post_update(request):
    return HttpResponse("<h1>Update</h1>")

def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")
