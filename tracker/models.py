from uuid import uuid4

from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

MIN_SCORE = 0
MAX_SCORE = 10


def validate_score(value):
    if not MIN_SCORE <= value <= MAX_SCORE:
        raise ValidationError(
            "{value} is not between {mns} and {mxs}".format(
                value=value, mns=MIN_SCORE, mxs=MAX_SCORE
            ),
        )


class MoodRecord(models.Model):
    id = models.CharField(default=uuid4, primary_key=True, max_length=256)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(validators=[validate_score])
    description = models.TextField(max_length=500, blank=True)
