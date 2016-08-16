from django.shortcuts import render
from django.core.mail import send_mail
from trydjango import settings
from .forms import ContactForm, SignUpForm

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

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # for key, value in form.cleaned_data.iteritems():
        #     print key, value
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        form_subject = "Site contact form"
        from_email = settings.EMAIL_HOST_USER
        # to_email = SignUp.objects.filter_by(email=email).all()
        contact_message = "%s: %s via %s" % (form_full_name, form_message, form_email)
        send_mail(
            form_subject,
            contact_message,
            from_email,
            ['jreiher2003@yahoo.com'],
            fail_silently=False,
        )
        # print email,message,full_name
    context = {"form": form}

    return render(request, "forms.html", context)