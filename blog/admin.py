from django.contrib import admin
from blog.models import Profile, Post, Category, Comment

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)

