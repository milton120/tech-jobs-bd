from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("User must have a password")
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.active = is_active
        user.staff = is_staff
        user.admin = is_admin
        user.save(using=self._db)

        return user   # returning user object after saving

    def create_stffuser(self, email, password=None):
        user = self.create_user(
            email,
            password,
            is_staff=True,
        )

        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password,
            is_staff=True,
            is_admin=True,
        )

        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    # below fields for future implementation
    # confirmed_email = models.BooleanField(varbose_name="confirmation by email", default=False)
    # activation_key = models.CharField(varbose_name="activation key for email", max_length=50)
    # activation_expires = models.DateTimeField(varbose_name="deadline of activation account", )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    # USERNAME_FIELD and password are required by default.
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin






