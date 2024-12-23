from django.db import models
from django.utils.timezone import now

class Feedback(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the user providing feedback")
    email = models.EmailField(help_text="Email of the user providing feedback")
    message = models.TextField(help_text="Feedback message")
    created_at = models.DateTimeField(default=now, editable=False, help_text="Timestamp when the feedback was submitted")

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"
        ordering = ['-created_at']

    def __str__(self):
        return f"Feedback from {self.name} ({self.email})"
