from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomUserManager(BaseUserManager):
<<<<<<< HEAD
    def create_user(self, email, name, password=None, **extra_fields):
=======
    def create_user(self, email, password=None, **extra_fields):
>>>>>>> a4b65654 (links)
        if not email:
            raise ValueError("Email is required")
        if not password:
            raise ValueError("Password is required")

        email = self.normalize_email(email)
<<<<<<< HEAD
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
=======
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Hash password properly
>>>>>>> a4b65654 (links)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        name = extra_fields.pop("name", None)
        if not name:
            raise ValueError("Superuser must have a name.")

        return self.create_user(email, name, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    preferences = models.JSONField(default=dict, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email
