#!/usr/bin/python
# -*- coding: utf-8 -*-

from zope.interface import implements
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from crgis.atcontents.interfaces import ITempleView

from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from Products.Archetypes.config import REFERENCE_CATALOG


class TempleView(BrowserView):
    """Default view of a Temple
    """
    implements(ITempleView)

    __call__ = ViewPageTemplateFile('temple.pt')

    def deity_term(self, value):
        factory = getUtility(IVocabularyFactory, 'deity_name')
        vocabulary = factory(self.context)
        try:
            existing = vocabulary.getTerm(value)
            return existing.title.split('，')[0]
        except LookupError:
            return value

    def t_title(self, vocab, value):
        factory = getUtility(IVocabularyFactory, vocab)
        vocabulary = factory(self.context)
        try:
            term = vocabulary.getTerm(value)
            return term.title
        except LookupError:
            return None

    def getTemplePilgrimage(self, temple):
        portal_catalog = getToolByName(self.context, 'portal_catalog')
        reference_catalog = getToolByName(self.context, REFERENCE_CATALOG)
        results = []
        # pil used here, but they are schedules actually.
        pil_uids = [r.sourceUID
                    for r in reference_catalog.searchResults(
                    targetUID=temple.UID(), relationship='temples_in_pilgrimage')]
        if pil_uids:
            pil_brains = portal_catalog.searchResults(
                portal_type='Schedule', UID=pil_uids, sort_on='sortable_title')
            for brain in pil_brains:
                url = brain.getURL()
                obj = brain.getObject()
                parent = obj.aq_inner.aq_parent
                full_title = parent.Title() + obj.Title()
                results.append(dict(
                    url = url,
                    full_title = full_title,
                ))
        return results

    def getTempleFestival(self, temple):
        portal_catalog = getToolByName(self.context, 'portal_catalog')
        reference_catalog = getToolByName(temple, REFERENCE_CATALOG)
        results = []
        fsv_uids = [r.sourceUID
                    for r in reference_catalog.searchResults(
                    targetUID=temple.UID(), relationship='relatesTo')]
        if fsv_uids:
            fsv_brains = portal_catalog.searchResults(
                portal_type='Event', UID=fsv_uids, sort_on='start', sort_order='ascending')
            for brain in fsv_brains:
                results.append(dict(
                    url = brain.getURL(),
                    full_title = str(brain.start)[:4]+'年'+brain.Title,
                ))
        return results

    def getTempleBiXieWu(self, temple):
        portal_catalog = getToolByName(self.context, 'portal_catalog')
        reference_catalog = getToolByName(temple, REFERENCE_CATALOG)
        results = []
        bxw_uids = [r.sourceUID
                    for r in reference_catalog.searchResults(
                    targetUID=temple.UID(), relationship='temple_bixiewu')]
        if bxw_uids:
            bxw_brains = portal_catalog.searchResults(
                portal_type='BiXieWu', UID=bxw_uids)
            for brain in bxw_brains:
                results.append(dict(
                    url = brain.getURL(),
                    title = brain.Title,
                ))
        return results

