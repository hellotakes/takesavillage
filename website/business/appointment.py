import datetime
import itertools
from typing import List, Iterable, Tuple

import attrs

from website.models.appointment import Appointment
from website.models.business_hours import BusinessHours


@attrs.define
class Slot:
    start: 'datetime.datetime'
    duration: 'datetime.timedelta'

    @property
    def end(self) -> 'datetime.datetime':
        return self.start + self.duration

    @property
    def time(self) -> 'datetime.time':
        return self.start.time()

    @property
    def date(self) -> 'datetime.date':
        return self.start.date()

    def overlaps(self, between: Tuple['datetime.datetime', 'datetime.datetime']):
        return between[0] <= self.start <= between[1] or between[0] <= self.end <= between[1] or self.start <= self.between[0] <= self.end

    def timestamp(self):
        return self.start.timestamp()


def group_slots_by_days(
        days: List['datetime.date'],
        slots: Iterable['Slot']
) -> Iterable[List['Slot']]:
    result = []

    sorted_slots = sorted(slots, key=lambda slot: slot.start)
    for day in days:
        day_slots = [slot for slot in sorted_slots if slot.date == day]
        result.append(day_slots)

    return list(itertools.zip_longest(*result, fillvalue=None))


def compute_available_slots(
        days: List['datetime.date'],
        business_hours: List['BusinessHours'],
        current_appointments: List['Appointment']
) -> Iterable['Slot']:
    return filter(
        lambda slot: is_slot_available(slot, current_appointments),
        compute_slots_for_days(days, business_hours)
    )


def is_slot_available(
        slot: 'Slot',
        current_appointments: List['Appointment']
) -> bool:
    for appointment in current_appointments:
        if slot.overlaps(appointment.between):
            return False

    return True


def compute_slots_for_days(
        days: List['datetime.date'],
        business_hours: List['BusinessHours'],
) -> Iterable['Slot']:
    return itertools.chain.from_iterable(
        compute_slots_for_day(day, business_hours) for day in days
    )


def compute_slots_for_day(
        day: 'datetime.date',
        business_hours: List['BusinessHours'],
) -> Iterable['Slot']:
    day_business_hours = next(
        (hours for hours in business_hours if hours.day_of_week == day.isoweekday()),
        None
    )
    if not day_business_hours:
        return []

    return itertools.chain(
        compute_slots_for_range(day, day_business_hours.session_duration, day_business_hours.morning_start, day_business_hours.morning_end),
        compute_slots_for_range(day, day_business_hours.session_duration, day_business_hours.afternoon_start, day_business_hours.afternoon_end),
    )


def compute_slots_for_range(
        day: 'datetime.date',
        session_duration: 'datetime.timedelta',
        _from: 'datetime.time',
        _to: 'datetime.time'
) -> Iterable['Slot']:
    first_slot = datetime.datetime.combine(day, _from)
    slots_gen = (Slot(duration=session_duration, start=first_slot + (session_duration * i)) for i in itertools.count())
    return itertools.takewhile(lambda slot: slot.time < _to, slots_gen)

