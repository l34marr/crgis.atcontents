from zope.interface import implements
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from crgis.atcontents.interfaces import IScheduleView

from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import base_hasattr


class ScheduleView(BrowserView):
    """Default view of a Schedule
    """
    implements(IScheduleView)

    __call__ = ViewPageTemplateFile('schedule.pt')

    def related_temples(self):
        context = aq_inner(self.context)
        res = ()
        if base_hasattr(context, 'getRawTemples'):
            catalog = getToolByName(context, 'portal_catalog')
            related = context.getRawTemples()
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

    def getPhoto(self, temple):
        catalog = getToolByName(self.context, 'portal_catalog')
        photo = catalog(portal_type = 'Photo',
                        review_state = ('published', 'external', 'internal', 'internally_published'),
                        path = {'query': '.'.join(temple.getPhysicalPath())}
                       )[:1]
        if len(photo) == 0:
            return None
        return photo[0].getObject()

