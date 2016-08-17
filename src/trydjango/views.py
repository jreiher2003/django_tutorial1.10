from django.shortcuts import render 
from newsletter.forms import ContactForm

def about(request):
    return render(request, "about.html", {})

def contact(request):
    title = "Contact Us"
    form = ContactForm(request.POST or None)
    if form.is_valid():
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
    context = {"form": form, "title": title}
    return render(request, "contact.html", context)