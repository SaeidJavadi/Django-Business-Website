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


def export_json(modeladmin, request, queryset):
    response = HttpResponse(content_type="application/json")
    serializers.serialize('json', queryset, stream=response)
    return response


make_active.short_description = _('Mark selected status as Active')
make_inactive.short_description = _('Mark selected status as Inactive')
export_json.short_description = _('Export selected as Json request')


class ImageInstanceInline(admin.TabularInline):
    model = models.AboutPic
    extra = 4


class TeamInstanceInline(admin.StackedInline):
    model = models.TeamInfo
    extra = 1


@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    inlines = (ImageInstanceInline, TeamInstanceInline)
    list_display = ('head1', 'head2', 'status')
    list_editable = ('status',)
    actions = (make_active, make_inactive, export_json)
