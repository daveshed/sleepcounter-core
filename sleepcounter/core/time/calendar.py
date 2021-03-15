"""
Defines the Calendar class which holds special events
"""
import logging

from sleepcounter.core.time import bedtime

LOGGER = logging.getLogger("calendar")


class Calendar:
    """
    Interface to the library of special events. It allows you to lookup the next
    event and find out what is happening today.
    """
    def __init__(self, events: list = None):
        self._date_library = events if events else []

    def add_event(self, event):
        """
        Add an event to the calendar

        keyword arguments:
        event -- an event instance
        """
        self._date_library.append(event)
        return self

    @staticmethod
    def seconds_to_event(event):
        """Returns the number of seconds to a given event"""
        return event.seconds_remaining

    @staticmethod
    def sleeps_to_event(event):
        """Return the number of sleeps to a given event"""
        return event.sleeps_remaining

    @property
    def events(self):
        """Returns all events objects in the calendar"""
        return [event for event in self._date_library if event.active]

    @events.setter
    def events(self, events: list):
        """Update events contained in the calendar to a list of event objects"""
        self._date_library = events

    @property
    def next_event(self):
        """Get the next event to happen"""
        deltas = \
            {ev: ev.seconds_remaining for ev in self.events}
        next_event = min(deltas, key=deltas.get)
        LOGGER.info("Next event is %s", next_event.name)
        return next_event

    @property
    def sleeps_to_next_event(self):
        """Return the number of sleeps to the next event"""
        return self.sleeps_to_event(self.next_event)

    @property
    def special_day_today(self):
        """
        Checks whether today is a special day registered in the calendar and
        returns the result as a bool
        """
        result = any(event.today for event in self.events)
        LOGGER.info("Today %s special", ("is" if result else "is not"))
        return result

    @property
    def todays_event(self):
        """Returns todays event or None if it's not a special day"""
        result = None
        for event in self._date_library:
            if event.today:
                result = event
                break
        LOGGER.info(
            "It's %s today",
            (result.name if result else "not a special day"))
        return result

    @property
    def seconds_to_next_event(self):
        """Returns the time to the next event in seconds"""
        seconds = self.seconds_to_event(self.next_event)
        LOGGER.info(
            "%s seconds to next event (%s)",
            seconds,
            self.next_event.name)
        return seconds

    @property
    def is_nighttime(self):
        """Checks whether it's nighttime and returns the result as a bool"""
        return bedtime.SleepChecker.is_nighttime()

    def _get_event(self, search_date):
        # get the event corresponding to a given search date
        result = None
        for event in self._date_library:
            if event.date == search_date:
                result = event
                return result
        return result
