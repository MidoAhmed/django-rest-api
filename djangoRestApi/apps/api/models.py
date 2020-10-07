from django.db import models


class Task(models.Model):
    class TaskStatus(models.TextChoices):
        INITIATED = "INITIATED"
        IN_PROGRESS = 'IN_PROGRESS'
        PENDING = "PENDING"
        COMPLETED = "COMPLETED"

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=100,
        choices=TaskStatus.choices,
        default=TaskStatus.INITIATED
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def is_opened(self):
        return self.status in {
            self.TaskStatus.INITIATED,
            self.TaskStatus.IN_PROGRESS,
        }
