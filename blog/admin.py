
# Register your models here.

from django.contrib import admin
from .models import *
from .models import Post, User
from django.contrib.auth.admin import UserAdmin
from .models import Profile
# admin.site.register(CustomUser)
from .models import Category
from .models import Comment

##########{

from .models import Tag
admin.site.register(Tag)
###########}



admin.site.register(Category)

# class UserAdmin(UserAdmin):
#     model = User
#     list_display = ('username', 'email', 'bio')
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'bio')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions', 'groups')}),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'email', 'password1', 'password2'),
#         }),
#     )
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Profile)

class PostAdmin(admin.ModelAdmin):
    list_display = ("title","author","slug")


admin.site.register(Post, PostAdmin)




