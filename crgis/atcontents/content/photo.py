"""Definition of the Photo content type
"""


from zope.interface import implements
from Products.CMFCore.permissions import View
from Products.CMFCore.permissions import ModifyPortalContent
from AccessControl import ClassSecurityInfo
from ComputedAttribute import ComputedAttribute

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content.image import ATImage

from plone.app.blob.content import ATBlob

from Products.ATContentTypes.interface import file as atfile
from Products.ATContentTypes.interface import image as atimage
from plone.app.blob.interfaces import IATBlobBlob, IATBlobFile, IATBlobImage

# -*- Message Factory Imported Here -*-
from crgis.atcontents import atcontentsMessageFactory as _

from crgis.atcontents.interfaces import IPhoto
from crgis.atcontents.config import PROJECTNAME

PhotoSchema = ATImage.schema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.LinesField(
        'category',
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label=_(u"Category"),
            description=_(u"Multiple Choices."),
        ),
        vocabulary_factory='category',
    ),

    atapi.LinesField(
        'attachesTo',
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label=_(u"Attached To"),
            description=_(u"Attached To Which Fields."),
        ),
        vocabulary_factory='attachesTo',
    ),

    atapi.StringField(
        'cou',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"County"),
            description=_(u"Enter Text."),
        ),
    ),

    atapi.StringField(
        'tow',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Town"),
            description=_(u"Enter Text."),
        ),
    ),

    atapi.StringField(
        'vil',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Village"),
            description=_(u"Enter Text."),
        ),
    ),

    atapi.StringField(
        'lng',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Longtitude"),
            description=_(u"Enter Longtitude."),
        ),
    ),

    atapi.StringField(
        'lat',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Latitude"),
            description=_(u"Enter Latitude."),
        ),
    ),

    atapi.StringField(
        'year',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Photo Year"),
            description=_(u"4 digits for Year."),
        ),
    ),

    atapi.StringField(
        'month',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Photo Month"),
            description=_(u"2 digits for Month."),
        ),
    ),

    atapi.StringField(
        'day',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Photo Day"),
            description=_(u"2 digits for Day."),
        ),
    ),

    atapi.StringField(
        'owner_name',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Owner Name"),
            description=_(u"Enter Owner Name."),
        ),
    ),

    atapi.StringField(
        'owner_org',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Owner Organization"),
            description=_(u"Enter Owner Organization."),
        ),
    ),

    atapi.StringField(
        'owner_title',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Owner Title"),
            description=_(u"Enter Owner Title."),
        ),
    ),

    atapi.TextField(
        'reference',
        storage=atapi.AnnotationStorage(),
        widget=atapi.RichWidget(
            label=_(u"Reference"),
            description=_(u"Enter Text."),
        ),
        default_output_type='text/x-html-safe',
    ),
), marshall=atapi.PrimaryFieldMarshaller())

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

PhotoSchema['title'].storage = atapi.AnnotationStorage()
PhotoSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(PhotoSchema, moveDiscussion=False)


class Photo(ATBlob):
    """Photo for CRGIS Contents"""
    
    implements(IPhoto, IATBlobImage, atimage.IATImage, atimage.IImageContent)
    
    security       = ClassSecurityInfo()
    
    meta_type = "Photo"
    schema = PhotoSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    #~ image = atapi.ATFieldProperty('image')
    category = atapi.ATFieldProperty('category')
    attachesTo = atapi.ATFieldProperty('attachesTo')
    cou = atapi.ATFieldProperty('cou')
    tow = atapi.ATFieldProperty('tow')
    vil = atapi.ATFieldProperty('vil')
    lng = atapi.ATFieldProperty('lng')
    lat = atapi.ATFieldProperty('lat')
    year = atapi.ATFieldProperty('year')
    month = atapi.ATFieldProperty('month')
    day = atapi.ATFieldProperty('day')
    owner_name = atapi.ATFieldProperty('owner_name')
    owner_org = atapi.ATFieldProperty('owner_org')
    owner_title = atapi.ATFieldProperty('owner_title')
    reference = atapi.ATFieldProperty('reference')


atapi.registerType(Photo, PROJECTNAME)
