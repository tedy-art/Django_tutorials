from django.db import models
from django.utils import timezone


# Create your models here.

class TaskStatus(models.TextChoices):
    COMPLETED = 'CO', 'Completed'  # making option/choices
    PENDING = 'PE', 'Pending'
    DROPPED = 'DR', 'Dropped'


class Tag(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(
        default=timezone.now()
    )
    completed_at = models.DateTimeField(null=True)
    deadline = models.DateTimeField(null=True, blank=True)
    # tag many to many
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.content

    status = models.CharField(
        choices=TaskStatus.choices,  # getting choices from TaskStatus
        default=TaskStatus.PENDING,  # mark status with pending choice
        max_length=2,
    )


"""
requirement:-
    1) user can add task
    2) a task can be tagged with one or more tags
    3) you can search task by content or a tag
    4) task can have urgency and importance
    5) task can have status 1) pending, 2) completed, 3) dropped

    Detect nouns -->
        1) Tag
        2) Task

    Detect attributes-->
        1) tasks = 1) content, 2)deadline, 3)created_at, 4)completed_at
        2) tag = 1) name
"""
