"""
A custom calendar that can be used to start up the application
"""
from sleepcounter.core.time.calendar import Calendar
from sleepcounter.core.time.event import SpecialDay, Anniversary

_DEFAULT_SLEEPS_TO_COUNT = 20

CUSTOM_DIARY = Calendar([
    Anniversary(
        name='Bonfire Night',
        month=11,
        day=5,
        sleeps=_DEFAULT_SLEEPS_TO_COUNT
    ),
    Anniversary(
        name='Halloween',
        month=10,
        day=31,
        sleeps=_DEFAULT_SLEEPS_TO_COUNT
    ),
    Anniversary(
        name='Christmas',
        month=12,
        day=25,
    ),
    SpecialDay(
        name='Legoland',
        year=2019,
        month=4,
        day=27,
        sleeps=_DEFAULT_SLEEPS_TO_COUNT
    ),
])
