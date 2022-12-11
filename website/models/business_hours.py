import datetime
from typing import Tuple

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class BusinessHours(models.Model):
    specialist = models.ForeignKey('website.Specialist', on_delete=models.CASCADE)
    day_of_week = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(7)])
    session_duration = models.DurationField()
    morning_start = models.TimeField()
    morning_end = models.TimeField()
    afternoon_start = models.TimeField()
    afternoon_end = models.TimeField()

    class Meta:
        ordering = ['day_of_week']

    @property
    def morning(self) -> Tuple['datetime.time', 'datetime.time']:
        return self.morning_start, self.morning_end

    @property
    def afternoon(self) -> Tuple['datetime.time', 'datetime.time']:
        return self.afternoon_start, self.afternoon_end
