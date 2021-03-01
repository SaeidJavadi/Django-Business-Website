from django.db import models
from django.utils.translation import gettext_lazy as _

STATUS_CHOICES = (
    ('active', _('active')),
    ('inactive', _('inactive')),
)

image_dir = r'../media/pictures'


class About(models.Model):
    head1 = models.CharField(max_length=120, verbose_name=_('Head 1'))
    head1_text = models.CharField(max_length=120, verbose_name=_('Text Head 1'), null=True, blank=True)
    head2 = models.CharField(max_length=200, verbose_name=_('Head 2'))
    head2_text = models.CharField(max_length=120, verbose_name=_('Text Head 2'), null=True, blank=True)
    head3 = models.CharField(max_length=120, verbose_name=_('Head 3'))
    head3_text = models.CharField(max_length=120, verbose_name=_('Text Head 3'), null=True, blank=True)
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


class AboutPic(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='about_pic')
    pic = models.ImageField(verbose_name=_('About Picture'), upload_to=image_dir)

    class Meta:
        verbose_name = _('Team Picture')
        verbose_name_plural = _('Teams Pictures')

    def __str__(self):
        return self.about.head1


class TeamInfo(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='about_team')
    img = models.ImageField(verbose_name=_('Profile Inmage'), upload_to=image_dir + r'/profile')
    name = models.CharField(max_length=120, verbose_name=_('Name'))
    bio = models.CharField(max_length=200, verbose_name=_('Bio'))
    fb = models.CharField(max_length=200, verbose_name=_('Facebook link'), blank=True, null=True)
    twitter = models.CharField(max_length=200, verbose_name=_('twitter link'), blank=True, null=True)
    ln = models.CharField(max_length=200, verbose_name=_('LinkedIn link'), blank=True, null=True)
    google = models.CharField(max_length=200, verbose_name=_('G+ link'), blank=True, null=True)

    class Meta:
        verbose_name = _('Team Info')
        verbose_name_plural = _('Teams Info')

    def __str__(self):
        return self.name


class Services(models.Model):
    head1 = models.CharField(max_length=200, verbose_name=_('Head 1'))
    head2 = models.CharField(max_length=200, verbose_name=_('Head 2'))
    head2_text = models.CharField(max_length=120, verbose_name=_('Text Head 2'), null=True, blank=True)
    proj_total = models.IntegerField(verbose_name=_('Total Projects'))
    proj_done = models.IntegerField(verbose_name=_('Projects Done'))
    img = models.ImageField(verbose_name=_('Image'), upload_to=image_dir + r'/service')
    img_head = models.CharField(max_length=200, verbose_name=_('Image Head'))
    img_text = models.TextField(verbose_name=_('Image Text'))
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default='inactive', verbose_name=_('Status'))

    class Meta:
        verbose_name = _('Service Page')
        verbose_name_plural = _('Services Page')

    def __str__(self):
        return self.head1


class ServicesTools(models.Model):
    servicehead = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='service_tools')
    avator = models.ImageField(verbose_name=_('Avator'), upload_to=image_dir)
    head_service = models.CharField(max_length=120, verbose_name=_('Service Head'))
    text_service = models.TextField(verbose_name=_('Text Service'))

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
    status = models.CharField(max_length=60, verbose_name=_('Status'),
                              choices=(('Read', _('Read')), ('UnRead', _('UnRead'))), default='UnRead')

    class Meta:
        verbose_name = _('Contact us')
        verbose_name_plural = _('Contact us')

    def __str__(self):
        return self.email


class Footer(models.Model):
    address = models.CharField(max_length=200, verbose_name=_('Address'))
    email = models.CharField(max_length=200, verbose_name=_('Email'))
    phone = models.CharField(max_length=200, verbose_name=_('Phone'))
    head = models.CharField(max_length=200, verbose_name=_('Contact Us Head'))
    logo = models.ImageField(verbose_name=_('Image'), upload_to=image_dir + r'/logo')
    fb = models.CharField(max_length=200, verbose_name=_('Facebook link'), blank=True, null=True)
    twitter = models.CharField(max_length=200, verbose_name=_('twitter link'), blank=True, null=True)
    ln = models.CharField(max_length=200, verbose_name=_('LinkedIn link'), blank=True, null=True)
    google = models.CharField(max_length=200, verbose_name=_('G+ link'), blank=True, null=True)
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default='inactive', verbose_name=_('Status'))

    class Meta:
        verbose_name = _('Footer Control')
        verbose_name_plural = _('Footer Control')


class Header(models.Model):
    logo = models.ImageField(verbose_name=_('Image'), upload_to=image_dir + r'/logo')
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default='inactive', verbose_name=_('Status'))

    class Meta:
        verbose_name = _('Header Control')
        verbose_name_plural = _('Header Control')

    def __str__(self):
        return str(self.id)


class Banners(models.Model):
    header = models.ForeignKey(Header, on_delete=models.CASCADE, related_name='header_banner')
    head1 = models.CharField(max_length=200, verbose_name=_('Head 1'))
    head2 = models.CharField(max_length=200, verbose_name=_('Head 2'))
    head2_text = models.CharField(max_length=120, verbose_name=_('Text Head 2'), null=True, blank=True)
    banner = models.ImageField(verbose_name=_('Image'), upload_to=image_dir + r'/banner')

    class Meta:
        verbose_name = _('Banner')
        verbose_name_plural = _('Banners')

    def __str__(self):
        return self.head1


class Newsletters(models.Model):
    email = models.CharField(max_length=120, verbose_name=_('Email'))
    joindate = models.DateTimeField(auto_now_add=True, verbose_name=_('Join Date'))

    class Meta:
        verbose_name = _('Newsletters')
        verbose_name_plural = _('Newsletters')

    def __str__(self):
        return self.email
