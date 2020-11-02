from django.contrib import admin

# Register your models here.

from .models import Post, Comment

# admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
	list_display = ('title','slug','status','created_on') # tuple
	list_filter = ('status',) # tuple
	search_fields = ['title','content'] # list
	prepopulated_fields = {'slug': ('title',)} # json, str value tuple key
admin.site.register(Post, PostAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active') # tuple
    list_filter = ('active', 'created_on') # tuple
    search_fields = ('name', 'email', 'body') # tuple
    actions = ['approve_comments'] # list, takes queryset and updates active boolean field to True

    def approve_comments(self, request, queryset):
        queryset.update(active=True)