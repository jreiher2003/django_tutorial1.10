from django.contrib import messages  
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render, get_object_or_404, redirect 
from .forms import PostForm 
from .models import Post 

# Create your views here.
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())
    # else:
    #     messages.error(request, "Not successfully created")
    context = {"form": form,}
    return render(request, "post_form.html", context)

def post_detail(request, id):
    instance = get_object_or_404(Post,id=id)
    context = {"title": "Detail Title", "instance": instance}
    return render(request, "post_detail.html", context)

def post_list(request):
    queryset = Post.objects.all()
    context = {"title": "List Title", "object_list": queryset}
    return render(request, "index.html", context)

def post_update(request, id=None):
    instance = get_object_or_404(Post,id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#'>successfully</a> edited", extra_tags="html_safe")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {"title": "Detail Title", "instance": instance, "form": form}
    return render(request, "post_form.html", context)

def post_delete(request, id=None):
    instance = get_object_or_404(Post,id=id)
    instance.delete()
    messages.success(request, "successfully deleted")
    return redirect("posts:post_list")
