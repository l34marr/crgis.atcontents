from zope.interface import implements
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from crgis.atcontents.interfaces import IPilgrimageView


class PilgrimageView(BrowserView):
    """Default view of a Pilgrimage
    """
    implements(IPilgrimageView)

    __call__ = ViewPageTemplateFile('pilgrimage.pt')

