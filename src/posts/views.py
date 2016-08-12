from urllib import quote_plus 
from django.contrib import messages  
from django.http import HttpResponse, HttpResponseRedirect, Http404 
from django.shortcuts import render, get_object_or_404, redirect 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.db.models import Q
from .forms import PostForm 
from .models import Post 

# Create your views here.
def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    # if not request.user.is_authenticated():
    #     raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {"form": form,}
    return render(request, "post_form.html", context)

def post_detail(request, slug):
    instance = get_object_or_404(Post,slug=slug)
    if instance.draft or instance.publish > timezone.now().date():
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    share_string = quote_plus(instance.content)
    context = {"title": "Detail Title", "instance": instance, "share_string":share_string}
    return render(request, "post_detail.html", context)

def post_list(request):
    today = timezone.now().date()
    queryset_list = Post.objects.active()#filter(draft=False).filter(publish__lte=timezone.now())#.all()#.order_by("-timestamp")
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Post.objects.all()
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query) 
            ).distinct()
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
    context = {"title": "List Title", "object_list": queryset, "today": today}
    return render(request, "index.html", context)


def post_update(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
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
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post,id=id)
    instance.delete()
    messages.success(request, "successfully deleted")
    return redirect("posts:post_list")
