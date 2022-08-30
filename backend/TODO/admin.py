from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class CustomUserModelAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email',)
    list_display_links = ('username',)
    search_fields = ('username', 'email',)

# class UsersAdmin(admin.ModelAdmin):
#     list_display = ('username', 'first_name', 'last_name', 'email', )
#     list_display_links = ('username', )
#     search_fields = ('username', 'email', )
#
#
# admin.site.register(User, UsersAdmin)
