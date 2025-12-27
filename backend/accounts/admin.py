from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import Group
from django.contrib import admin
from accounts.models import User
from django.utils.translation import gettext_lazy as _


class UsersAdmin(BaseUserAdmin):
    form = UserChangeForm
    form_add = UserCreationForm
    list_display = ('email', 'full_name', 'phone', 'is_admin')
    fieldsets = (
        (_('main'), {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('phone', 'full_name', 'idcode', 'dateofbirth')}),
        (_('Permissions'), {'fields': ('is_active', 'is_admin','email_confirm', 'phone_confirm')})
    )

    add_fieldsets = (
        (None, {'fields': ('email', 'full_name', 'dateofbirth', 'phone','idcode', 'password1', 'password2')}),
    )
    search_fields = ('email', 'full_name',)
    ordering = ('phone',)
    filter_horizontal = ()
    list_filter = ('is_admin',)


admin.site.register(User, UsersAdmin)
admin.site.unregister(Group)
