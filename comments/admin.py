from django.contrib import admin
from .models import CommentingUser, Comment

# Register your models here.
admin.site.register(CommentingUser)
admin.site.register(Comment)