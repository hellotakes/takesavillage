from django.core.validators import MaxValueValidator
from django.db import models


class BusinessHours(models.Model):
    specialist = models.ForeignKey('website.Specialist', on_delete=models.CASCADE)
    day_of_week = models.PositiveIntegerField(validators=[MaxValueValidator(6)])
    session_duration = models.DurationField()
    morning_start = models.TimeField()
    morning_end = models.TimeField()
    afternoon_start = models.TimeField()
    afternoon_end = models.TimeField()

    class Meta:
        ordering = ['day_of_week']
