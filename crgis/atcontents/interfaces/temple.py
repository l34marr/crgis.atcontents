from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from crgis.atcontents import atcontentsMessageFactory as _


class ITempleView(Interface):
    """Marker for browser view of Temple
    """

class ITemple(Interface):
    """Temple Type"""

