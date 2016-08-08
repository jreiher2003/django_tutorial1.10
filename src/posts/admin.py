from django.contrib import admin
from .models import Post
# Register your models here.
# create customize admin port
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "timestamp", "updated"]
    list_display_links = ["title"]
    list_filter = ["title", "timestamp"]
    search_fields = ["title", "content"]
    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)

