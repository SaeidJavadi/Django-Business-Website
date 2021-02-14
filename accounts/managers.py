from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, full_name, phone, password):
        if not email:
            raise ValueError('کاربران باید حتما ایمیل داشته باشند')
        if not full_name:
            raise ValueError('نام و نام خانوادگی باید وارد شود')
        if not phone:
            raise ValueError('شماره موبایل باید وارد شود')
        # if not dateofbirth:
        #     raise ValueError('تاریخ تولد باید وارد شود')

        user = self.model(email=self.normalize_email(email), full_name=full_name, phone=phone)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, phone, password):
        user = self.create_user(email=email, full_name=full_name, phone=phone,
                                password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user
