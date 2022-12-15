import datetime
from typing import Tuple

from django.db import models


class Appointment(models.Model):
    specialist = models.ForeignKey("website.models.caregiver.Caregiver", on_delete=models.PROTECT)
    parent = models.ForeignKey("website.Parent", on_delete=models.PROTECT)
    from_time = models.DateTimeField()
    duration = models.DurationField()
    booked_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.specialist.full_name}  {self.from_time} ({self.parent})"

    @property
    def end(self) -> 'datetime.datetime':
        return self.from_time + self.duration

    @property
    def between(self) -> Tuple['datetime.datetime', 'datetime.datetime']:
        return self.from_time, self.end
