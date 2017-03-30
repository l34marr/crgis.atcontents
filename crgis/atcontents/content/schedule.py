"""Definition of the Schedule content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from archetypes.referencebrowserwidget import ReferenceBrowserWidget

from crgis.atcontents import atcontentsMessageFactory as _

from crgis.atcontents.interfaces import ISchedule
from crgis.atcontents.interfaces import ITemple
from crgis.atcontents.config import PROJECTNAME

ScheduleSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    atapi.TextField(
        'body',
        storage=atapi.AnnotationStorage(),
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            label=_(u"Body"),
            rows = 20,
        ),
    ),

    atapi.ReferenceField(
        'temples',
        widget=ReferenceBrowserWidget(
            label=_(u"Related Temples"),
            allow_browse=1,
            allow_sorting=1,
            startup_directory='/temples',
        ),
        multiValued=1,
        relationship="temples_in_pilgrimage",
        index='KeywordIndex',
        referencesSortable=1,
    ),

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

ScheduleSchema['title'].storage=atapi.AnnotationStorage()
ScheduleSchema['description'].storage=atapi.AnnotationStorage()
ScheduleSchema['title'].widget.label=_(u'Schedule Title')
ScheduleSchema['effectiveDate'].widget.label=_(u'Schedule StartDate')
ScheduleSchema['effectiveDate'].widget.description=_(u'Schedule StartDate Description')
ScheduleSchema['expirationDate'].widget.visible={'edit': 'invisible', 'view': 'invisible'}
ScheduleSchema['language'].widget.visible={'edit': 'invisible', 'view': 'invisible'}

schemata.finalizeATCTSchema(
    ScheduleSchema,
    moveDiscussion=False
)


class Schedule(base.ATCTContent):
    """Schedule ContentType"""
    implements(ISchedule)

    meta_type = "Schedule"
    schema = ScheduleSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    body = atapi.ATFieldProperty('body')
    temples = atapi.ATFieldProperty('temples')

atapi.registerType(Schedule, PROJECTNAME)

