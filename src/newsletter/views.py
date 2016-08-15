from django.shortcuts import render
from .forms import SignUpForm

# Create your views here.
def home(request):
    form = SignUpForm(request.POST or None)
    title = "Welcome"
    context = {"title": title,"form": form}
    if form.is_valid():
        # form.save() save stright away
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New full name"
        instance.full_name = full_name

        # check instance here
        instance.save()
        context = {"title": "Thank You"}
    return render(request, "home.html", context)