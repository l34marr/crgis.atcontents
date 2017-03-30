from zope.interface import Interface
from zope import schema

from crgis.atcontents import atcontentsMessageFactory as _


class IPilgrimageView(Interface):
    """Marker for browser view of Pilgrimage
    """

class IPilgrimage(Interface):
    """Pilgrimage ContentType
    """

