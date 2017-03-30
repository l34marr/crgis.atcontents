## Controller Python Script "folder_rename"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=paths=[],new_titles=[],new_owners=[],new_dates_y=[],new_dates_m=[],new_dates_d=[]
##title=Photo Metadata
##

from Products.CMFPlone.utils import transaction_note
from Products.CMFPlone import PloneMessageFactory as _
from ZODB.POSException import ConflictError
from Products.PythonScripts.standard import url_unquote

portal = context.portal_url.getPortalObject()
request = context.REQUEST

message = None
putils = context.plone_utils

for x in range(0, len(paths)):
    path = paths[x]
    title = new_titles[x]
    owner = new_owners[x]
    y = new_dates_y[x]
    m = new_dates_m[x]
    d = new_dates_d[x]
    obj = portal.restrictedTraverse(path)
    obj.update(title=title, owner_name=owner, year=y, month=m, day=d)

if message is None:
    message = _(u'Metadata changed.')

context.plone_utils.addPortalMessage(message)
return state
