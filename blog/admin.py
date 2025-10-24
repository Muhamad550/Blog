from django.contrib import admin
from .models import BlogPost, Category, Comment

# Category Admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    search_fields = ['name']

# BlogPost Admin  
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'category', 'created_at']
    list_filter = ['category', 'author', 'created_at']
    search_fields = ['title', 'content']
    readonly_fields = ['created_at', 'updated_at']

# Comment Admin
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'author', 'created_at']
    list_filter = ['post', 'author', 'created_at']
    search_fields = ['content']

# Register models
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)