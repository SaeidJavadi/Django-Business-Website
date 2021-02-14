from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, full_name, dateofbirth, phone, password):
        if not email:
            raise ValueError(_('Users must have an email '))
        if not full_name:
            raise ValueError(_('Name must be entered'))
        if not phone:
            raise ValueError(_('Mobile number must be entered'))
        if not dateofbirth:
            raise ValueError(_('Date of birth must be entered'))

        user = self.model(email=self.normalize_email(email), full_name=full_name, phone=phone, dateofbirth=dateofbirth)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, phone, password, dateofbirth):
        user = self.create_user(email=email, full_name=full_name, dateofbirth=dateofbirth, phone=phone,
                                password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user
