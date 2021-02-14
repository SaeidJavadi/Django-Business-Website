from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.contrib.auth.models import Group
from accounts.models import User
from accounts.forms import UserChangeForm, UserCreationForm


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    form_add = UserCreationForm
    list_display = ('email', 'full_name', 'phone', 'is_admin')
    fieldsets = (
        ('main', {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('phone', 'full_name', 'dateofbirth')}),
        ('Permissions', {'fields': ('is_active', 'is_admin')})
    )

    add_fieldsets = (
        (None, {'fields': ('email', 'full_name', 'dateofbirth', 'phone', 'password1', 'password2')}),
    )
    search_fields = ('email', 'full_name', 'email')
    ordering = ('phone',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
