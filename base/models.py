from django.db import models
from django.utils.translation import gettext_lazy as _

STATUS_CHOICES = (
    ('active', _('active')),
    ('inactive', _('inactive')),
)

image_dir  = '..\media\pictures'

class Pictures(models.Model):
    pic = models.ImageField(verbose_name=_('Picture'), upload_to=image_dir)

    class Meta:
        verbose_name = _('Picture')
        verbose_name_plural = _('Pictures')


class About(models.Model):
    head1 = models.CharField(max_length=200, verbose_name=_('Head 1'))
    head1_text = models.TextField(verbose_name=_('Text Head 1'))
    head2 = models.CharField(max_length=200, verbose_name=_('Head 2'))
    head2_text = models.TextField(verbose_name=_('Text Head 2'))
    img = models.ImageField(verbose_name=_('Image'), upload_to=image_dir)
    img_head = models.CharField(max_length=200, verbose_name=_('Image Head'))
    img_text = models.TextField(verbose_name=_('Image Text'))
    plain_text = models.TextField(verbose_name=_('Plain Text'))
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default='inactive', verbose_name=_('Status'))

    class Meta:
        verbose_name = _('About')
        verbose_name_plural = _('About')

    def __str__(self):
        return self.head1

class ServiceHead(models.Model):
    head1 = models.CharField(max_length=200, verbose_name=_('Head 1'))
    head2 = models.CharField(max_length=200, verbose_name=_('Head 2'))

    class Meta:
        verbose_name = _('Service Page')
        verbose_name_plural = _('Services Page')

    def __str__(self):
        return self.head1

class Services(models.Model):
    avator = models.ImageField(verbose_name=_('Avator'),upload_to=image_dir)
    head_service = models.CharField(max_length=120, verbose_name=_('Service Head'))
    text_service = models.TextField(verbose_name=_('Text Service'))
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default='active')

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    def __str__(self):
        return self.head_service

class Contact(models.Model):
    name = models.CharField(max_length=120, verbose_name=_('Name'))
    email = models.EmailField(verbose_name=_('Email'))
    phone = models.IntegerField(verbose_name=_('Phone Number'))
    message = models.TextField(verbose_name=_('Message'))

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

    def __str__(self):
        return self.email


