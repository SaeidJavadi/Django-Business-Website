from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from accounts.managers import UserManager

class User(AbstractBaseUser):
    email = models.EmailField(max_length=120, unique=True, verbose_name='ایمیل')
    full_name = models.CharField(max_length=120, verbose_name='نام و نام خانوادگی')
    dateofbirth = models.DateField(verbose_name='تاریخ تولد', null=True, blank=True)
    phone = models.IntegerField(verbose_name='شماره تلفن')
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'phone']

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
        verbose_name = 'کاربر'
        verbose_name_plural ='کاربران'


