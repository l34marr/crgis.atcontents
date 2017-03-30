## Controller Python Script "validate_folder_rename"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=paths=[],new_titles=[],new_owners=[],new_dates_y=[],new_dates_m=[],new_dates_d=[]
##title=Validate folder renaming
##

from Products.CMFPlone import PloneMessageFactory as _

paths=[path for path in paths if path]
new_titles=[title for title in new_titles]

if len(paths)!=len(new_titles):
    context.plone_utils.addPortalMessage(_(u'You must provide content titles'), 'error')
    return state.set(status='failure')

if state.getErrors():
    context.plone_utils.addPortalMessage(_(u'Please correct the indicated errors.'), 'error')
    return state.set(status='failure')

return state
