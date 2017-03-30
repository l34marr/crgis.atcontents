from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from crgis.atcontents import atcontentsMessageFactory as _



class IPhoto(Interface):
    """Photo for CRGIS Contents"""

    # -*- schema definition goes here -*-
    category = schema.List(
        title=_(u"Category"),
        required=False,
        description=_(u"Multiple Choices."),
    )
#
    cou = schema.TextLine(
        title=_(u"County"),
        required=False,
        description=_(u"Enter Text."),
    )
#
    tow = schema.TextLine(
        title=_(u"Town"),
        required=False,
        description=_(u"Enter Text."),
    )
#
    vil = schema.TextLine(
        title=_(u"Village"),
        required=False,
        description=_(u"Enter Text."),
    )
#
    lng = schema.TextLine(
        title=_(u"Longtitude"),
        required=False,
        description=_(u"Enter Longtitude."),
    )
#
    lat = schema.TextLine(
        title=_(u"Latitude"),
        required=False,
        description=_(u"Enter Latitude."),
    )
#
    year = schema.TextLine(
        title=_(u"Photo Year"),
        required=False,
        description=_(u"Enter Text."),
    )
#
    month = schema.TextLine(
        title=_(u"Photo Month"),
        required=False,
        description=_(u"Enter Text."),
    )
#
    day = schema.TextLine(
        title=_(u"Photo Day"),
        required=False,
        description=_(u"Enter Text."),
    )
#
    owner_name = schema.TextLine(
        title=_(u"Owner Name"),
        required=False,
        description=_(u"Enter Owner Name."),
    )
#
    owner_org = schema.TextLine(
        title=_(u"Owner Organization"),
        required=False,
        description=_(u"Enter Owner Organization."),
    )
#
    owner_title = schema.TextLine(
        title=_(u"Owner Title"),
        required=False,
        description=_(u"Enter Owner Title."),
    )
#
    reference = schema.SourceText(
        title=_(u"Reference"),
        required=False,
        description=_(u"Enter Text."),
    )
#
