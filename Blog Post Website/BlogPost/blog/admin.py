from django.contrib import admin
from .models import Post, Comments

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'updated')
    list_filter = ('status', 'created', 'updated')
    # searching on the basis of author, and author is username
    search_fields = ('title', 'body', 'author__username')
    prepopulated_fields =  {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('comment', 'post', 'updated', 'active')
    list_filter = ('active', 'created')
    date_hierarchy = 'updated'
    raw_id_fields = ('post',)