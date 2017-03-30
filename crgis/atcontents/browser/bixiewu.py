from zope.interface import implements
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from crgis.atcontents.interfaces import IBiXieWuView

from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import base_hasattr

class BiXieWuView(BrowserView):
    """Default view of a BiXieWu
    """
    implements(IBiXieWuView)

    __call__ = ViewPageTemplateFile('bixiewu.pt')

    def t_title(self, vocab, value):
        factory = getUtility(IVocabularyFactory, vocab)
        vocabulary = factory(self.context)
        try:
            term = vocabulary.getTerm(value)
            return term.title
        except LookupError:
            return None

    def related_temples(self):
        context = aq_inner(self.context)
        res = ()
        if base_hasattr(context, 'getRawR_temples'):
            catalog = getToolByName(context, 'portal_catalog')
            related = context.getRawR_temples()
            if not related:
                return ()
            brains = catalog(UID=related)
            if brains:
                positions = dict([(v, i) for (i, v) in enumerate(related)])
                res = list(brains)
                def _key(brain):
                    return positions.get(brain.UID, -1)
                res.sort(key=_key)
        return res

