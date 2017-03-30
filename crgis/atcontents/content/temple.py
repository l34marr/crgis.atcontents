#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Definition of the Temple content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory

from crgis.atcontents import atcontentsMessageFactory as _

from crgis.atcontents.interfaces import ITemple
from crgis.atcontents.config import PROJECTNAME

TempleSchema = folder.ATFolderSchema.copy() + atapi.Schema((

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
        'facing',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Sitting Facing"),
            description=_(u"for example North 20 degree."),
        ),
    ),

    atapi.LinesField(
        'deity_host',
        searchable=1,
        required=0,
        index='KeywordIndex',
        multiValued=1,
        storage=atapi.AnnotationStorage(),
        vocabulary_factory='deity_name',
        enforceVocabulary=0,
        widget=atapi.MultiSelectionWidget(
            label=_(u"Deity Host"),
            description=_(u"Multiple Lines, One Per Line."),
        ),
    ),

    atapi.StringField(
        'deity_host_o',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Deity Host Other"),
            description=_(u"Self Description, Deity Host."),
        ),
    ),

    atapi.StringField(
        'deity_host_a',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Deity Host Alias"),
            description=_(u"Self Description, Deity Host Alias."),
        ),
    ),

    atapi.LinesField(
        'deity_company',
        searchable=1,
        required=0,
        index='KeywordIndex',
        multiValued=1,
        storage=atapi.AnnotationStorage(),
        vocabulary_factory='deity_name',
        enforceVocabulary=0,
        widget=atapi.MultiSelectionWidget(
            label=_(u"Deity Company"),
            description=_(u"Multiple Lines, One Per Line."),
        ),
    ),

    atapi.StringField(
        'religion',
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label=_(u"Religion Type"),
            description=_(u"Registry by Ministry of the Interior."),
            format='radio',
        ),
        vocabulary_factory='religion',
    ),

    atapi.StringField(
        'religion_o',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Religion Type Other"),
            description=_(u"Self Description, Religion Type."),
        ),
    ),

    atapi.StringField(
        'building',
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label=_(u"Building Type"),
            description=_(u"Single Choice."),
            format='radio',
        ),
        vocabulary_factory='building',
    ),

    atapi.StringField(
        'building_o',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Building Type Other"),
            description=_(u"Self Description, Building Type."),
        ),
    ),

    atapi.StringField(
        'registered',
        searchable=1,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Registered Name"),
            description=_(u"Registry by Ministry of the Interior."),
        ),
    ),

    atapi.StringField(
        'funding',
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label=_(u"Funding Type"),
            description=_(u"Registry by Ministry of the Interior."),
            format='radio',
        ),
        vocabulary_factory='funding',
    ),

    atapi.StringField(
        'organizing',
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label=_(u"Organizing Type"),
            description=_(u"Registry by Ministry of the Interior."),
            format='radio',
        ),
        vocabulary_factory='organizing',
    ),

    atapi.StringField(
        'organizing_o',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Organizing Type Other"),
            description=_(u"Self Description, Organizing Type."),
        ),
    ),

    atapi.StringField(
        'address',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Address"),
            description=_(u"Registry by Ministry of the Interior."),
        ),
    ),

    atapi.StringField(
        'in_charge',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Person In Charge"),
            description=_(u"Registry by Ministry of the Interior."),
        ),
    ),

    atapi.StringField(
        'tel',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Telephone"),
            description=_(u"Registry by Ministry of the Interior."),
        ),
    ),

    atapi.StringField(
        'homepage',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Homepage"),
        ),
    ),

    atapi.StringField(
        'era',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Estimated Earliest Founding Year"),
            description=_(u"Enter Estimated Earliest Founding Year in Western Calendar."),
        ),
    ),

    atapi.StringField(
        'era_end',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Estimated Latest Founding Year"),
            description=_(u"Enter Estimated Latest Founding Year in Western Calendar."),
        ),
    ),

    atapi.StringField(
        'year_accuracy',
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label=_(u"Year Accuracy"),
            description=_(u"Single Choice."),
            format='radio',
        ),
        vocabulary_factory='year_accuracy',
    ),

    atapi.TextField(
        'history',
        searchable=1,
        storage=atapi.AnnotationStorage(),
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            label=_(u"Establishment History"),
            description=_(u"Enter Establishment History."),
            rows = 20,
        ),
    ),

    atapi.StringField(
        'era_1',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Established Year by Taiwan Temple Collection"),
            description=_(u"Registry by Taiwan Temple Collection."),
        ),
    ),

    atapi.StringField(
        'era_2',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Established Year by Taiwan Temple Overview"),
            description=_(u"Registry by Taiwan Temple Overview."),
        ),
    ),

    atapi.TextField(
        'era_ref',
        storage=atapi.AnnotationStorage(),
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            label=_(u"References on Establishment"),
            description=_(u"Enter References on Establishment."),
            rows = 20,
        ),
    ),

    atapi.TextField(
        'deity_accompany',
        storage=atapi.AnnotationStorage(),
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            label=_(u"Deities Accompany"),
            description=_(u"Enter Deities Accompany."),
            rows = 20,
        ),
    ),

    atapi.TextField(
        'worship',
        storage=atapi.AnnotationStorage(),
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            label=_(u"Worship"),
            description=_(u"Enter Worship."),
            rows = 20,
        ),
    ),

    atapi.TextField(
        'introduction',
        storage=atapi.AnnotationStorage(),
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            label=_(u"Introduction"),
            description=_(u"Enter Introduction and Photo."),
            rows = 20,
        ),
    ),

    atapi.TextField(
        'overview',
        storage=atapi.AnnotationStorage(),
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            label=_(u"Building Overview"),
            description=_(u"Enter Building Overview."),
            rows = 20,
        ),
    ),

    atapi.TextField(
        'antiquity',
        storage=atapi.AnnotationStorage(),
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            label=_(u"Antiquities"),
            description=_(u"Enter Antiquities."),
            rows = 20,
        ),
    ),

    atapi.TextField(
        'narrate',
        storage=atapi.AnnotationStorage(),
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            label=_(u"Narrate"),
            description=_(u"Enter Narrate."),
            rows = 20,
        ),
    ),

    atapi.TextField(
        'non_narrate',
        storage=atapi.AnnotationStorage(),
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            label=_(u"Non Narrate"),
            description=_(u"Enter Non Narrate."),
            rows = 20,
        ),
    ),

    atapi.TextField(
        'academic',
        storage=atapi.AnnotationStorage(),
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            label=_(u"Academic Works"),
            description=_(u"Enter Academic Works."),
            rows = 20,
        ),
    ),

    atapi.TextField(
        'literature',
        storage=atapi.AnnotationStorage(),
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            label=_(u"Literature Reference"),
            description=_(u"Enter Literature Reference."),
            rows = 20,
        ),
    ),

    atapi.StringField(
        'fill_in',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Filling Person"),
            description=_(u"Enter Filling Person Name."),
        ),
    ),

    atapi.StringField(
        'fill_date',
        storage=atapi.AnnotationStorage(),
        widget=atapi.CalendarWidget(
            label=_(u"Filling Date"),
            description=_(u"Enter Date."),
        ),
    ),

    atapi.StringField(
        'jstq',
        storage=atapi.AnnotationStorage(),
        widget=atapi.MultiSelectionWidget(
            label=_(u"JiSiZuQun"),
            description=_(u"Multiple Choices."),
            format='checkbox',
        ),
        vocabulary_factory='jstq',
        schemata='appendix',
    ),

    atapi.StringField(
        'jstq_o',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"JiSiZuQun Other"),
            description=_(u"Self Description."),
        ),
        schemata='appendix',
    ),

    atapi.TextField(
        'jsfw',
        storage=atapi.AnnotationStorage(),
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            label=_(u"JiSiFanWei"),
            description=_(u"JiSiFanWei Description."),
            rows = 20,
        ),
        schemata='appendix',
    ),

    atapi.TextField(
        'xyfw',
        storage=atapi.AnnotationStorage(),
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            label=_(u"XinYangFanWei"),
            description=_(u"XingYangFanWei Description."),
            rows = 20,
        ),
        schemata='appendix',
    ),

    atapi.StringField(
        'flxt',
        storage=atapi.AnnotationStorage(),
        widget=atapi.MultiSelectionWidget(
            label=_(u"FenLingXiTong"),
            description=_(u"Multiple Choices."),
            format='checkbox',
        ),
        vocabulary_factory='flxt',
        schemata='appendix',
    ),

    atapi.StringField(
        'flxt_o',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"FenLingXiTong Other"),
            description=_(u"Self Description, for example MaZu."),
        ),
        schemata='appendix',
    ),

    atapi.StringField(
        'ymmy',
        storage=atapi.AnnotationStorage(),
        widget=atapi.MultiSelectionWidget(
            label=_(u"YiMingMiaoYu"),
            description=_(u"Multiple Choices."),
            format='checkbox',
        ),
        vocabulary_factory='ymmy',
        schemata='appendix',
    ),

    atapi.StringField(
        'ymmy_o',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"YiMingMiaoYu Other"),
            description=_(u"Self Description."),
        ),
        schemata='appendix',
    ),

    atapi.StringField(
        'xhly',
        storage=atapi.AnnotationStorage(),
        widget=atapi.MultiSelectionWidget(
            label=_(u"XiangHuoLaiYuan"),
            description=_(u"Multiple Choices."),
            format='checkbox',
        ),
        vocabulary_factory='xhly',
        schemata='appendix',
    ),

    atapi.StringField(
        'xhly_o',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"XiangHuoLaiYuan Other"),
            description=_(u"Self Description."),
        ),
        schemata='appendix',
    ),

    atapi.StringField(
        'nlqs',
        storage=atapi.AnnotationStorage(),
        widget=atapi.MultiSelectionWidget(
            label=_(u"NianLiQingSheng"),
            description=_(u"Multiple Choices."),
            format='checkbox',
        ),
        vocabulary_factory='nlqs',
        schemata='appendix',
    ),

    atapi.StringField(
        'nlqs_o',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"NianLiQingSheng Other"),
            description=_(u"Self Description."),
        ),
        schemata='appendix',
    ),

    atapi.StringField(
        'wyxx',
        storage=atapi.AnnotationStorage(),
        widget=atapi.MultiSelectionWidget(
            label=_(u"WangYeXianXiang"),
            description=_(u"Multiple Choices."),
            format='checkbox',
        ),
        vocabulary_factory='wyxx',
        schemata='appendix',
    ),

    atapi.StringField(
        'wyxx_o',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"WangYeXianXiang Other"),
            description=_(u"Self Description."),
        ),
        schemata='appendix',
    ),

    atapi.StringField(
        'medicine',
        storage=atapi.AnnotationStorage(),
        widget=atapi.MultiSelectionWidget(
            label=_(u"Medicine Divination"),
            description=_(u"Multiple Choices."),
        ),
        vocabulary_factory='medicine',
        schemata='appendix',
    ),

    atapi.StringField(
        'luck',
        storage=atapi.AnnotationStorage(),
        widget=atapi.MultiSelectionWidget(
            label=_(u"Luck Divination"),
            description=_(u"Multiple Choices."),
        ),
        vocabulary_factory='luck',
        schemata='appendix',
    ),

    atapi.TextField(
        'organization',
        storage=atapi.AnnotationStorage(),
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            label=_(u"Believer Organization"),
            description=_(u"Troupe, Music Hall."),
            rows = 20,
        ),
        schemata='appendix',
    ),

    atapi.TextField(
        'desc_o',
        storage=atapi.AnnotationStorage(),
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(
            label=_(u"Description Other"),
            description=_(u"Other Remarkable Description."),
            rows = 20,
        ),
        schemata='appendix',
    ),

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

TempleSchema['id'].widget.label=_(u"Code")
TempleSchema['id'].widget.description=_(u"A String Based on Abbreviation of Administrative Area.")
TempleSchema['title'].storage=atapi.AnnotationStorage()
TempleSchema['description'].storage=atapi.AnnotationStorage()
TempleSchema['title'].widget.label=_(u'Temple Title')
TempleSchema['description'].widget.visible={'edit': 'invisible', 'view': 'invisible'}

schemata.finalizeATCTSchema(
    TempleSchema,
    folderish=True,
    moveDiscussion=False
)


class Temple(folder.ATFolder):
    """Temple Type"""
    implements(ITemple)

    meta_type = "Temple"
    schema = TempleSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    data_src = atapi.ATFieldProperty('data_src')
    coordinate = atapi.ATFieldProperty('coordinate')
    facing = atapi.ATFieldProperty('facing')
    deity_host = atapi.ATFieldProperty('deity_host')
    deity_host_o = atapi.ATFieldProperty('deity_host_o')
    deity_host_a = atapi.ATFieldProperty('deity_host_a')
    deity_company = atapi.ATFieldProperty('deity_company')
    religion = atapi.ATFieldProperty('religion')
    religion_o = atapi.ATFieldProperty('religion_o')
    building = atapi.ATFieldProperty('building')
    building_o = atapi.ATFieldProperty('building_o')
    registered = atapi.ATFieldProperty('registered')
    funding = atapi.ATFieldProperty('funding')
    organizing = atapi.ATFieldProperty('organizing')
    organizing_o = atapi.ATFieldProperty('organizing_o')
    address = atapi.ATFieldProperty('address')
    in_charge = atapi.ATFieldProperty('in_charge')
    tel = atapi.ATFieldProperty('tel')
    homepage = atapi.ATFieldProperty('homepage')
    era = atapi.ATFieldProperty('era')
    era_end = atapi.ATFieldProperty('era_end')
    year_accuracy = atapi.ATFieldProperty('year_accuracy')
    history = atapi.ATFieldProperty('history')
    era_1 = atapi.ATFieldProperty('era_1')
    era_2 = atapi.ATFieldProperty('era_2')
    era_ref = atapi.ATFieldProperty('era_ref')
    deity_accompany = atapi.ATFieldProperty('deity_accompany')
    worship = atapi.ATFieldProperty('worship')
    introduction = atapi.ATFieldProperty('introduction')
    overview = atapi.ATFieldProperty('overview')
    antiquity = atapi.ATFieldProperty('antiquity')
    narrate = atapi.ATFieldProperty('narrate')
    non_narrate = atapi.ATFieldProperty('non_narrate')
    academic = atapi.ATFieldProperty('academic')
    literature = atapi.ATFieldProperty('literature')
    fill_in = atapi.ATFieldProperty('fill_in')
    fill_date = atapi.ATFieldProperty('fill_date')
    jstq = atapi.ATFieldProperty('jstq')
    jstq_o = atapi.ATFieldProperty('jstq_o')
    jsfw = atapi.ATFieldProperty('jsfw')
    xyfw = atapi.ATFieldProperty('xyfw')
    flxt = atapi.ATFieldProperty('flxt')
    flxt_o = atapi.ATFieldProperty('flxt_o')
    ymmy = atapi.ATFieldProperty('ymmy')
    ymmy_o = atapi.ATFieldProperty('ymmy_o')
    xhly = atapi.ATFieldProperty('xhly')
    xhly_o = atapi.ATFieldProperty('xhly_o')
    nlqs = atapi.ATFieldProperty('nlqs')
    nlqs_o = atapi.ATFieldProperty('nlqs_o')
    wyxx = atapi.ATFieldProperty('wyxx')
    wyxx_o = atapi.ATFieldProperty('wyxx_o')
    medicine = atapi.ATFieldProperty('medicine')
    luck = atapi.ATFieldProperty('luck')
    organization = atapi.ATFieldProperty('organization')
    desc_o = atapi.ATFieldProperty('desc_o')

    def deity_term(self, value):
        factory = getUtility(IVocabularyFactory, 'deity_name')
        vocabulary = factory(self)
        try:
            existing = vocabulary.getTerm(value)
            return existing.title.split(u'，')[0]
        except LookupError:
            return value

atapi.registerType(Temple, PROJECTNAME)
