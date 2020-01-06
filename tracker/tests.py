import pytest

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase

import factory.django

from tracker.models import MoodRecord
from tracker.models import MIN_SCORE, MAX_SCORE

pytestmark = pytest.mark.django_db


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = "chris"


def test_can_create_moodrecord():
    # make a user
    kirkman = UserFactory()

    record = MoodRecord(user=kirkman, score=5, description="Feel just okay")
    record.save()
    record_id = record.id
    record = MoodRecord.objects.get(id=record_id)
    assert record.score == 5, "scores do not match"
    assert record.description == "Feel just okay", "description does not match"
    assert record.user == kirkman


def test_relationships():
    # make a user
    kirkman = UserFactory()

    for i in range(10):
        record = MoodRecord(user=kirkman, score=i + 1)
        record.save()

    assert kirkman.moodrecord_set.count() == 10

    kirkman.moodrecord_set.all().delete()
    assert kirkman.moodrecord_set.count() == 0

    kirkman.moodrecord_set.add(MoodRecord(score=10), bulk=False)
    assert kirkman.moodrecord_set.first().score == 10
