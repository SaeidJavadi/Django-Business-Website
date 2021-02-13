from django.contrib import admin
from django.contrib.auth.models import Group
from accounts.models import User
from accounts.forms import UserChangeForm, RegisterUserForm, RegisterFormAdmin

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserChangeForm
    form_add = RegisterFormAdmin
    list_display = ('email', 'full_name', 'phone', 'is_admin')
    fieldsets = (
        ('main', {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('phone', 'full_name', 'dateofbirth')}),
        ('Permissions', {'fields': ('is_active', 'is_admin')})
    )

    add_fieldsets = (
        (None, {'fields': ('email', 'full_name', 'dateofbirth', 'phone', 'password')}),
    )
    search_fields = ('email', 'full_name', 'email')
    ordering = ('phone',)
    filter_horizontal = ()
