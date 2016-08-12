from django.contrib import messages  
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render, get_object_or_404, redirect 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PostForm 
from .models import Post 

# Create your views here.
def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {"form": form,}
    return render(request, "post_form.html", context)

def post_detail(request, slug):
    instance = get_object_or_404(Post,slug=slug)
    context = {"title": "Detail Title", "instance": instance}
    return render(request, "post_detail.html", context)

def post_list(request):
    queryset_list = Post.objects.all()#.order_by("-timestamp")
    paginator = Paginator(queryset_list, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {"title": "List Title", "object_list": queryset}
    return render(request, "index.html", context)


def post_update(request, slug=None):
    instance = get_object_or_404(Post,slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
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
