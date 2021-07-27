import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    """Question model."""
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        """Return str representation."""
        return self.question_text

    def was_published_recently(self):
        """Returns True if publish date is within a day."""
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    """Model for a question's choices."""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """Return str representation."""
        return self.choice_text
