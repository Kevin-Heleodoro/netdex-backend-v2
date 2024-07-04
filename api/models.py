from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    # Override the related_name for groups and user_permissions
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_set",  # Custom related_name
        blank=True,
        help_text="The groups this user belongs to.",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_set",  # Custom related_name
        blank=True,
        help_text="Specific permissions for this user.",
        related_query_name="user",
    )

    def __str__(self):
        return self.user_name


class Note(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    note = models.TextField()


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True, null=True)
    social_media = models.URLField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    notes = models.ManyToManyField(Note, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
