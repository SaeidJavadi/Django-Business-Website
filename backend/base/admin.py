from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.core import serializers
from django.http import HttpResponse
from base import models


def make_active(modeladmin, request, queryset):
    result = queryset.update(status='active')
    m1 = _("change status was")
    message_bit = "{} {}".format(result, m1)
    m2 = _("successfuly marked as Active")
    modeladmin.message_user(request, "{} {}.".format(message_bit, m2))


def make_inactive(modeladmin, request, queryset):
    result = queryset.update(status='inactive')
    m1 = _("change status was")
    message_bit = "{} {}".format(result, m1)
    m2 = _("successfuly marked as Inactive")
    modeladmin.message_user(request, "{} {}.".format(message_bit, m2))


def make_read(modeladmin, request, queryset):
    result = queryset.update(status='Read')
    m1 = _("change status was")
    message_bit = "{} {}".format(result, m1)
    m2 = _("successfuly marked as Read")
    modeladmin.message_user(request, "{} {}.".format(message_bit, m2))


def make_unread(modeladmin, request, queryset):
    result = queryset.update(status='UnRead')
    m1 = _("change status was")
    message_bit = "{} {}".format(result, m1)
    m2 = _("successfuly marked as UnRead")
    modeladmin.message_user(request, "{} {}.".format(message_bit, m2))


def export_json(modeladmin, request, queryset):
    response = HttpResponse(content_type="application/json")
    serializers.serialize('json', queryset, stream=response)
    return response


make_active.short_description = _('Mark selected status as Active')
make_inactive.short_description = _('Mark selected status as Inactive')
make_read.short_description = _('Mark selected status as Read')
make_unread.short_description = _('Mark selected status as UnRead')
export_json.short_description = _('Export selected as Json request')


class ImageInstanceInline(admin.TabularInline):
    model = models.AboutPic
    extra = 1


class TeamInstanceInline(admin.StackedInline):
    model = models.TeamInfo
    extra = 1


class BannerInstanceInline(admin.StackedInline):
    model = models.Banners
    extra = 1


@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    inlines = (ImageInstanceInline, TeamInstanceInline)
    list_display = ('head1', 'head2', 'status')
    list_editable = ('status',)
    actions = (make_active, make_inactive, export_json)


class ServiceToolsInstanceInline(admin.StackedInline):
    model = models.ServicesTools
    extra = 1


@admin.register(models.Services)
class ServiceAdmin(admin.ModelAdmin):
    inlines = (ServiceToolsInstanceInline,)
    list_display = ('head1', 'head2', 'proj_total', 'proj_done', 'status')
    list_editable = ('status', 'proj_total', 'proj_done')
    actions = (make_active, make_inactive, export_json)


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message', 'status')
    list_editable = ('status',)
    actions = (export_json, make_read, make_unread)


@admin.register(models.Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'address', 'status')
    list_editable = ('status',)
    actions = (make_active, make_inactive, export_json)


@admin.register(models.Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')
    list_editable = ('status',)
    actions = (make_active, make_inactive, export_json)
    inlines = (BannerInstanceInline,)


@admin.register(models.Newsletters)
class NewslettersAdmin(admin.ModelAdmin):
    list_display = ('email','joindate')
    actions = (export_json,)
