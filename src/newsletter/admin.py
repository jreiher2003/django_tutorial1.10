from django.contrib import admin
from .forms import SignUpForm 
from .models import SignUp
# Register your models here.
# create customize admin port
class SignUpModelAdmin(admin.ModelAdmin):
    list_display = ["email", "full_name", "timestamp", "updated"]
    list_display_links = ["email"]
    list_filter = ["email", "timestamp", "full_name"]
    search_fields = ["email", "full_name", "timestamp"]
    # class Meta:
    #     model = SignUp
    form = SignUpForm

admin.site.register(SignUp, SignUpModelAdmin)
