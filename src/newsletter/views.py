from django.shortcuts import render
from django.core.mail import send_mail
from trydjango import settings
from .forms import ContactForm, SignUpForm
from .models import SignUp

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
    if request.user.is_authenticated() and request.user.is_staff:
        query = SignUp.objects.all()
        context = {
            "queryset": query
        }
    return render(request, "home.html", context)

def example(request):
    return render(request, "example.html", {})
