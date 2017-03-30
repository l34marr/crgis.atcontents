"""Definition of the BiXieWu content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from archetypes.referencebrowserwidget import ReferenceBrowserWidget
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from crgis.atcontents import atcontentsMessageFactory as _

from crgis.atcontents.interfaces import IBiXieWu
from crgis.atcontents.config import PROJECTNAME

BiXieWuSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    atapi.StringField(
        'data_src',
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label=_(u"Data Source"),
            description=_(u"Single Choice."),
            format='radio',
        ),
        vocabulary_factory='data_src',
    ),

    atapi.StringField(
        'lct_cou',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"County"),
            description=_(u"Enter Text."),
        ),
    ),

    atapi.StringField(
        'lct_tow',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Town"),
            description=_(u"Enter Text."),
        ),
    ),

    atapi.StringField(
        'lct_vil',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Village"),
            description=_(u"Enter Text."),
        ),
    ),

    atapi.StringField(
        'coordinate',
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label=_(u"Coordinate Type"),
            description=_(u"Single Choice."),
            format='radio',
        ),
        vocabulary_factory='coordinate',
    ),

    atapi.StringField(
        'type',
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label=_(u"BiXieWu Type"),
            description=_(u"Single Choice."),
            format='radio',
        ),
        vocabulary_factory='bixiewu',
    ),

    atapi.StringField(
        'era',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Common Era"),
            description=_(u"Enter Common Era."),
        ),
        # validators=('isInt'),
    ),

    atapi.TextField(
        'era_ref',
        storage=atapi.AnnotationStorage(),
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            label=_(u"Era Reference"),
            description=_(u"Enter Era Reference."),
        ),
    ),

    atapi.StringField(
        'facing',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Facing"),
            description=_(u"Enter Facing."),
        ),
        # validators=('isInt'),
    ),

    atapi.StringField(
        'material',
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label=_(u"Material"),
            description=_(u"Single Choice."),
            format='radio',
        ),
        vocabulary_factory='material',
    ),

    atapi.TextField(
        'volume',
        storage=atapi.AnnotationStorage(),
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            label=_(u"Volume"),
            description=_(u"Enter Volume Description."),
        ),
    ),

    atapi.StringField(
        'locational',
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label=_(u"Locational Attribute"),
            description=_(u"Single Choice."),
            format='radio',
        ),
        vocabulary_factory='locational',
    ),

    atapi.LinesField(
        'purpose',
        searchable=1,
        multiValued=1,
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label=_(u"Purpose"),
            description=_(u"Multiple Choice. Primary Choice Goes First."),
        ),
        vocabulary_factory='purpose',
    ),

    atapi.TextField(
        'worship',
        storage=atapi.AnnotationStorage(),
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            label=_(u"Worship Description"),
            description=_(u"Enter Text."),
        ),
    ),

    atapi.TextField(
        'establishment',
        storage=atapi.AnnotationStorage(),
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            label=_(u"Establishment Description"),
            description=_(u"Enter Text."),
        ),
    ),

    atapi.TextField(
        'spatial',
        storage=atapi.AnnotationStorage(),
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            label=_(u"Spatial Attribute"),
            description=_(u"Enter Spatial Attributes."),
        ),
    ),

    atapi.TextField(
        'environment',
        storage=atapi.AnnotationStorage(),
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            label=_(u"Environmental Description"),
            description=_(u"Enter Environmental Description."),
        ),
    ),

    atapi.TextField(
        'reference',
        storage=atapi.AnnotationStorage(),
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            label=_(u"Reference"),
            description=_(u"Enter Text."),
        ),
    ),

    atapi.TextField(
        'remark',
        storage=atapi.AnnotationStorage(),
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            label=_(u"Remark"),
            description=_(u"Enter Text."),
        ),
    ),

    atapi.ReferenceField(
        'r_temples',
        widget=ReferenceBrowserWidget(
            label=_(u"Related Temples"),
            force_close_on_insert=1,
            allow_browse=1,
            allow_sorting=1,
            startup_directory='/temples/KinmenCounty',
        ),
        multiValued=1,
        relationship="temple_bixiewu",
        index='KeywordIndex',
        referencesSortable=1,
    ),

    atapi.StringField(
        'village',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Village Name"),
            description=_(u"Enter Village."),
        ),
        schemata='fengshiye',
    ),

    atapi.StringField(
        'color',
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label=_(u"Color"),
            description=_(u"Single Choice."),
        ),
        vocabulary_factory='isExisting',
        schemata='fengshiye',
    ),

    atapi.StringField(
        'genre',
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label=_(u"Genre"),
            description=_(u"Single Choice."),
        ),
        vocabulary_factory='genre',
        schemata='fengshiye',
    ),

    atapi.StringField(
        'posture',
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label=_(u"Posture"),
            description=_(u"Single Choice."),
            format='radio',
        ),
        vocabulary_factory='posture',
        schemata='fengshiye',
    ),

    atapi.StringField(
        'gender',
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label=_(u"Gender"),
            description=_(u"Single Choice."),
        ),
        vocabulary_factory='gender',
        schemata='fengshiye',
    ),

    atapi.StringField(
        'shi_d',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"ShiZi Depth"),
            description=_(u"In CentiMeter."),
        ),
        validators=('isInt'),
        schemata='fengshiye',
    ),

    atapi.StringField(
        'shi_w',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"ShiZi Width"),
            description=_(u"In CentiMeter."),
        ),
        validators=('isInt'),
        schemata='fengshiye',
    ),

    atapi.StringField(
        'shi_h',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"ShiZi Height"),
            description=_(u"In CentiMeter."),
        ),
        validators=('isInt'),
        schemata='fengshiye',
    ),

    atapi.StringField(
        'shi_t',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"ShiZi Head"),
            description=_(u"In CentiMeter."),
        ),
        validators=('isInt'),
        schemata='fengshiye',
    ),

    atapi.StringField(
        'base_l',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Base Length"),
            description=_(u"In CentiMeter."),
        ),
        validators=('isInt'),
        schemata='fengshiye',
    ),

    atapi.StringField(
        'base_w',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Base Width"),
            description=_(u"In CentiMeter."),
        ),
        validators=('isInt'),
        schemata='fengshiye',
    ),

    atapi.StringField(
        'base_h',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Base Height"),
            description=_(u"In CentiMeter."),
        ),
        validators=('isInt'),
        schemata='fengshiye',
    ),

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

BiXieWuSchema['id'].widget.label=_(u"Code")
BiXieWuSchema['id'].widget.description=_(u"A String Based on Abbreviation of Administrative Area.")
BiXieWuSchema['title'].storage=atapi.AnnotationStorage()
BiXieWuSchema['description'].storage=atapi.AnnotationStorage()
BiXieWuSchema['title'].widget.label=_(u'BiXieWu Title')
BiXieWuSchema['description'].widget.visible={'edit': 'invisible', 'view': 'invisible'}

schemata.finalizeATCTSchema(
    BiXieWuSchema,
    folderish=True,
    moveDiscussion=False
)


class BiXieWu(folder.ATFolder):
    """BiXieWu ContentType"""
    implements(IBiXieWu)

    meta_type = "BiXieWu"
    schema = BiXieWuSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    data_src = atapi.ATFieldProperty('data_src')
    lct_cou = atapi.ATFieldProperty('lct_cou')
    lct_tow = atapi.ATFieldProperty('lct_tow')
    lct_vil = atapi.ATFieldProperty('lct_vil')
    coordinate = atapi.ATFieldProperty('coordinate')
    type = atapi.ATFieldProperty('type')
    era = atapi.ATFieldProperty('era')
    era_ref = atapi.ATFieldProperty('era_ref')
    facing = atapi.ATFieldProperty('facing')
    material = atapi.ATFieldProperty('material')
    volume = atapi.ATFieldProperty('volume')
    locational = atapi.ATFieldProperty('locational')
    purpose = atapi.ATFieldProperty('purpose')
    worship = atapi.ATFieldProperty('worship')
    establishment = atapi.ATFieldProperty('establishment')
    spatial = atapi.ATFieldProperty('spatial')
    environment = atapi.ATFieldProperty('environment')
    reference = atapi.ATFieldProperty('reference')
    remark = atapi.ATFieldProperty('remark')
    r_temples = atapi.ATFieldProperty('r_temples')
    village = atapi.ATFieldProperty('village')
    color = atapi.ATFieldProperty('color')
    genre = atapi.ATFieldProperty('genre')
    posture = atapi.ATFieldProperty('posture')
    gender = atapi.ATFieldProperty('gender')
    shi_d = atapi.ATFieldProperty('shi_d')
    shi_w = atapi.ATFieldProperty('shi_w')
    shi_h = atapi.ATFieldProperty('shi_h')
    shi_t = atapi.ATFieldProperty('shi_t')
    base_l = atapi.ATFieldProperty('base_l')
    base_w = atapi.ATFieldProperty('base_w')
    base_h = atapi.ATFieldProperty('base_h')


atapi.registerType(BiXieWu, PROJECTNAME)
