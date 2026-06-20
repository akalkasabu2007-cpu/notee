from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class note(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField()
    CATEGORY_CHOICES = [
        ('work', 'Work'),
        ('personal', 'Personal'),
        ('other', 'Other'),
    ]
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notes',
        null=True,
        blank=True,
    )
    taskname = models.CharField(max_length=200, blank=True, default='')
    taskdesc = models.TextField(blank=True, default='')
    taskdate = models.DateField(null=True, blank=True)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='other'
    )
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.Title

