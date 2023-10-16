from django.db import models

# Create your models here.

"""
requirement :-
    1) user can add tasks
    2) a task can be tagged with one or more tages
    3) you can search for tasks by content or by a tag
    4) task can have urgency and an importance
    5) tasks can have a status -> pending, completed or dropped
    
# Detect nouns --> those nouns going to be a table/entity name :-
    1) Task 2) tag
    
# Detect Attributes and relationship
    tasks --> content, deadline, created_at, completed_at
    tag --> name, tag have relationship with tasks Many --> Many
"""


class Tag(models.Model):
    name = models.CharField(max_length=225)


class Task(models.Model):  # here task is going to be a table
    content = models.TextField()  # content is going to be a column
    deadline = models.DateTimeField()
    created_at = models.DateTimeField()
    completed_at = models.DateTimeField()
    tags = models.ManyToManyField(Tag)

    class TaskStatus(models.TextChoices):
        COMPLETED = 'CO', 'completed'
        PENDING = 'PE', 'Pending'
        DROPPED = 'DR', 'Dropped'

    status = models.CharField(
        choices=TaskStatus.choices,
        default=TaskStatus.PENDING,
        max_length=2,
    )  # must have a restricted set of choices
