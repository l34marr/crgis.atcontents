from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from crgis.atcontents import atcontentsMessageFactory as _


class IBiXieWuView(Interface):
    """Marker for browser view of BiXieWu
    """

class IBiXieWu(Interface):
    """BiXieWu ContentType"""

    # -*- schema definition goes here -*-
    data_src = schema.TextLine(
        title=_(u"Data Source"),
        required=False,
        description=_(u"Single Choice."),
    )
#
    lct_cou = schema.TextLine(
        title=_(u"County"),
        required=False,
        description=_(u"Enter Text."),
    )
#
    lct_tow = schema.TextLine(
        title=_(u"Town"),
        required=False,
        description=_(u"Enter Text."),
    )
#
    lct_vil = schema.TextLine(
        title=_(u"Village"),
        required=False,
        description=_(u"Enter Text."),
    )
#
    coordinate = schema.TextLine(
        title=_(u"Coordinate Type"),
        required=False,
        description=_(u"Single Choice."),
    )
#
    type = schema.TextLine(
        title=_(u"BiXieWu Type"),
        required=False,
        description=_(u"Single Choice."),
    )
#
    era = schema.TextLine(
        title=_(u"Common Era"),
        required=False,
        description=_(u"Enter Common Era."),
    )
#
    era_ref = schema.SourceText(
        title=_(u"Era Reference"),
        required=False,
        description=_(u"Enter Era Reference."),
    )
#
    facing = schema.TextLine(
        title=_(u"Facing"),
        required=False,
        description=_(u"Enter Facing."),
    )
#
    material = schema.TextLine(
        title=_(u"Material"),
        required=False,
        description=_(u"Single Choice."),
    )
#
    volume = schema.SourceText(
        title=_(u"Volume"),
        required=False,
        description=_(u"Enter Volume Description."),
    )
#
    locational = schema.TextLine(
        title=_(u"Locational Attribute"),
        required=False,
        description=_(u"Single Choice."),
    )
#
    purpose = schema.TextLine(
        title=_(u"Purpose"),
        required=False,
        description=_(u"Single Choice."),
    )
#
    worship = schema.SourceText(
        title=_(u"Worship Description"),
        required=False,
        description=_(u"Enter Text."),
    )
#
    establishment = schema.SourceText(
        title=_(u"Establishment Description"),
        required=False,
        description=_(u"Enter Text."),
    )
#
    spatial = schema.SourceText(
        title=_(u"Spatial Attribute"),
        required=False,
        description=_(u"Enter Spatial Attributes."),
    )
#
    environment = schema.SourceText(
        title=_(u"Environmental Description"),
        required=False,
        description=_(u"Enter Environmental Description."),
    )
#
    reference = schema.SourceText(
        title=_(u"Reference"),
        required=False,
        description=_(u"Enter Text."),
    )
#
    remark = schema.SourceText(
        title=_(u"Remark"),
        required=False,
        description=_(u"Enter Text."),
    )
#
    village = schema.TextLine(
        title=_(u"Village Name"),
        required=False,
        description=_(u"Enter Village."),
    )
#
    color = schema.TextLine(
        title=_(u"Color"),
        required=False,
        description=_(u"Single Choice."),
    )
#
    genre = schema.TextLine(
        title=_(u"Genre"),
        required=False,
        description=_(u"Single Choice."),
    )
#
    posture = schema.TextLine(
        title=_(u"Posture"),
        required=False,
        description=_(u"Single Choice."),
    )
#
    gender = schema.TextLine(
        title=_(u"Gender"),
        required=False,
        description=_(u"Single Choice."),
    )
#
    shi_d = schema.TextLine(
        title=_(u"ShiZi Depth"),
        required=False,
        description=_(u"In CentiMeter."),
    )
#
    shi_w = schema.TextLine(
        title=_(u"ShiZi Width"),
        required=False,
        description=_(u"In CentiMeter."),
    )
#
    shi_h = schema.TextLine(
        title=_(u"ShiZi Height"),
        required=False,
        description=_(u"In CentiMeter."),
    )
#
    shi_t = schema.TextLine(
        title=_(u"ShiZi Head"),
        required=False,
        description=_(u"In CentiMeter."),
    )
#
    base_l = schema.TextLine(
        title=_(u"Base Length"),
        required=False,
        description=_(u"In CentiMeter."),
    )
#
    base_w = schema.TextLine(
        title=_(u"Base Width"),
        required=False,
        description=_(u"In CentiMeter."),
    )
#
    base_h = schema.TextLine(
        title=_(u"Base Height"),
        required=False,
        description=_(u"In CentiMeter."),
    )
#
