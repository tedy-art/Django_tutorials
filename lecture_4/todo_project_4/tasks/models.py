from django.db import models
from django.utils import timezone


# Create your models here.

class TaskStatus(models.TextChoices):
    COMPLETED = 'CO', 'Completed'
    PENDING = 'PE', 'Pending'
    DROPPED = 'DR', 'Dropped'


class Tag(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        # gives a human-readable representation of the object
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(
        default=timezone.now()
    )
    completed_at = models.DateTimeField(null=True)
    deadline = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=2,
        choices=TaskStatus.choices,
        default=TaskStatus.PENDING,
    )
    tags = models.ManyToManyField(Tag, null=True, blank=True)

    def __str__(self):
        return f"{self.content}"


    @property
    def foo(self):
        return 'hello'