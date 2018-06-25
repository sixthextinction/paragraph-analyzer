from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "analysis", "analyzed_at"]
    list_display_links = ["slug"]
    list_filter = ["analyzed_at"]
    search_fields = ["slug"]


admin.site.register(Post, PostAdmin)