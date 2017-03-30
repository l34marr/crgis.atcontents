from Products.CMFCore.utils import getToolByName
from zope.component import getMultiAdapter

request = container.REQUEST
catalog = getToolByName(context, 'portal_catalog')
portal_state = getMultiAdapter((context, request),
                               name=u'plone_portal_state')
path = portal_state.navigation_root_path() + '/temple/KinmenCounty'

for brain in catalog(portal_type='Temple', path=path):
    try:
        obj = brain.getObject()
        print "%s %s" % (obj.Title(), obj.getEra())
    except:
        pass
return printed
