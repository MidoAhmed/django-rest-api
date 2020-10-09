from django.db import models


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
    #userId = models.IntegerField(blank=True, null=True, default=None)
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
