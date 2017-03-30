from zope.interface import Interface
from zope import schema

from crgis.atcontents import atcontentsMessageFactory as _


class IScheduleView(Interface):
    """Marker for browser view of Schedule
    """

class ISchedule(Interface):
    """Schedule ContentType
    """

