from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from accounts.managers import UserManager
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser):
    email = models.EmailField(max_length=120, unique=True, verbose_name=_('Email'))
    email_confirm = models.BooleanField(default=False, verbose_name=_('Email Confirm'))
    full_name = models.CharField(max_length=120, verbose_name=_('First And Last Name'))
    dateofbirth = models.DateField(verbose_name=_('Date Of Birth'))
    phone = models.IntegerField(verbose_name=_('Phone Number'), unique=True)
    phone_confirm = models.BooleanField(default=False, verbose_name=_('Phone Confirm'))
    idcode = models.IntegerField(verbose_name=_('ID Code'), unique=True)
    is_admin = models.BooleanField(default=False, verbose_name=_('is Admin'))
    is_active = models.BooleanField(default=True, verbose_name=_('is Active'))

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'phone', 'dateofbirth', 'idcode']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        # permissions = [
        #     ("change_task_status", "Can change the status of tasks"),
        #     ("close_task", "Can remove a task by setting its status as closed"),
        # ]


class ConfirmCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('User'), related_name='user_code')
    email_code = models.IntegerField(verbose_name=_('Email Code'))
    phone_code = models.IntegerField(verbose_name=_('Phone Code'))

    def __str__(self):
        return self.user.full_name

    class Meta:
        verbose_name = _('Confirm Code')
        verbose_name_plural = _('Confirm Codes')
