from django.contrib import admin

# Register your models here.
from comments.models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Comment admin."""

    list_display = ('id', 'user', 'post', 'comment')