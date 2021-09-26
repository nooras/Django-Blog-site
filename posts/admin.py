from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "content"]
    list_display_links = ["content"]
    list_filter = ["updated"]
    list_editable = ["title"]
    search_fields = ["title", "content"]
    class Meta:
        model = Post

admin.site.register(Post)
