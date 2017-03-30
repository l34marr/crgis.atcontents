"""Definition of the Pilgrimage content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from crgis.atcontents import atcontentsMessageFactory as _

from crgis.atcontents.interfaces import IPilgrimage
from crgis.atcontents.config import PROJECTNAME

PilgrimageSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    atapi.TextField(
        'body',
        storage=atapi.AnnotationStorage(),
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            label=_(u"Body"),
            rows = 20,
        ),
    ),

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

PilgrimageSchema['title'].storage=atapi.AnnotationStorage()
PilgrimageSchema['description'].storage=atapi.AnnotationStorage()
PilgrimageSchema['title'].widget.label=_(u'Pilgrimage Title')
PilgrimageSchema['effectiveDate'].widget.label=_(u'Pilgrimage StartDate')
PilgrimageSchema['effectiveDate'].widget.description=_(u'Pilgrimage StartDate Description')
PilgrimageSchema['expirationDate'].widget.visible={'edit': 'invisible', 'view': 'invisible'}
PilgrimageSchema['language'].widget.visible={'edit': 'invisible', 'view': 'invisible'}

schemata.finalizeATCTSchema(
    PilgrimageSchema,
    folderish=True,
    moveDiscussion=False
)


class Pilgrimage(folder.ATFolder):
    """Pilgrimage ContentType"""
    implements(IPilgrimage)

    meta_type = "Pilgrimage"
    schema = PilgrimageSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    body = atapi.ATFieldProperty('body')

atapi.registerType(Pilgrimage, PROJECTNAME)

