from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from . models import Post

'''
class UserAdmin(admin.ModelAdmin):
    list_display = list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff')

'''
'''
class CustomUserAdmin(UserAdmin):
    def __init__(self, *args, **kwargs):
        super(UserAdmin, self).__init__(*args, **kwargs)
        UserAdmin.list_display = list(UserAdmin.list_display) + ['id']
'''

UserAdmin.list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Post)
