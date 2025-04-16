from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now


User = get_user_model()

class Content(models.Model):
    TYPE_CHOICES = [
        ('nerd', 'Nerd'),
        ('politics', 'Politics'),
        ('books', 'Books'),
        ('movies', 'Movies'),
        ('love', 'Love'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contents')
    content = models.TextField()
    content_type = models.CharField(max_length = 30, choices=TYPE_CHOICES)
    created_at = models.DateTimeField(default = now)

    answer_type = models.CharField(
        max_length=20,
        choices=[('user', 'User'), ('AI', 'AI')],
        default='user'
    )

    def __str__(self):
        return f"{self.content_type} - {self.user.username}"