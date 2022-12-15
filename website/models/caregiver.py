from django.contrib.postgres.fields import ArrayField
from django.db import models

from website.models.choices import Sex, Language


class Caregiver(models.Model):
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=240)
    email = models.EmailField(max_length=240)

    sex = models.CharField(max_length=1, choices=Sex.choices)
    address = models.OneToOneField(
        'website.CaregiverAddress',
        on_delete=models.PROTECT
    )

    profile_photo = models.ImageField(upload_to="caregivers/profile/")
    profile_video = models.URLField()

    languages = ArrayField(
        models.CharField(max_length=2, choices=Language.choices),
        size=3
    )
    description = models.TextField(max_length=640)

    physical = models.BooleanField(default=True)
    online = models.BooleanField(default=False)
    conditions = ArrayField(
        models.CharField(max_length=128),
        size=5
    )

    ranking = models.FloatField()
    number_comments = models.PositiveIntegerField()

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

