from django.contrib import admin
from .models import *
from .models import Post, User
from django.contrib.auth.admin import UserAdmin
from .models import Profile
from .models import Category
from .models import Comment
from .models import Tag
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Profile)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title","author","slug")

admin.site.register(Post, PostAdmin)




