from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.is_admin = False
        user.is_staff = False
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that suppors using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class TaskStatus(models.TextChoices):
    INITIATED = "INITIATED"
    IN_PROGRESS = 'IN_PROGRESS'
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=100,
        choices=TaskStatus.choices,
        default=TaskStatus.INITIATED
    )
    created = models.DateTimeField(auto_now_add=True)
    # userId = models.IntegerField(blank=True, null=True, default=None)
    user_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

    def is_opened(self):
        return self.status in {
            TaskStatus.INITIATED,
            TaskStatus.IN_PROGRESS,
        }

    def __repr__(self):
        return '<Task object ({}) "{}" "{}">'.format(self.id, self.title, self.description)
