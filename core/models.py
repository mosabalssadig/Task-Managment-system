from datetime import datetime, date
import django
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.


class user(AbstractUser):
    objects = UserManager()
    fullname = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    is_superuser = models.BooleanField(default=False)
    att = models.ForeignKey(
        'attendance_info', db_constraint=False, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.id}  -  {self.username}"


class profile(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    age = models.DateField(max_length=255)
    marital_status = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    grade = models.CharField(max_length=255)
    joining_date = models.DateField(default=django.utils.timezone.now)
    department = models.CharField(max_length=255)
    contract_type = models.CharField(max_length=255)
    internal_company_level = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id}  -  {self.user.username}"


class attendance_info(models.Model):
    userAtendance = models.ForeignKey(user, on_delete=models.CASCADE)
    in_time = models.DateField(default=django.utils.timezone.now)
    out_time = models.DateField(blank=True, null=True)
    total_duration = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.userAtendance}"


class task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateField()
    end_time = models.DateField()
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title}"


class report(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    report = models.TextField()
    filed = models.DateField(default=django.utils.timezone.now)
