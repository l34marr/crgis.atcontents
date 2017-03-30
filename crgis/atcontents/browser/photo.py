
from ..interfaces import IPhoto

from Products.TinyMCE.utility import TinyMCE


def getImageScales(self, field=None, context=None):
    if IPhoto.providedBy(context):
        field = context.getField('photo')
        scales = self.orig_getImageScales(field, context)
        for scale in scales:
            scale['value'] = scale['value'].replace('photo_', 'image_')
        return scales
    return self.orig_getImageScales(field, context)

TinyMCE.orig_getImageScales = TinyMCE.getImageScales
TinyMCE.getImageScales = getImageScales


from zope.interface import implements
from zope.component import getUtility

try:
    import json
except:
    import simplejson as json

# Not available in xml.etree
from elementtree import HTMLTreeBuilder

from Products.TinyMCE.adapters.JSONDetails import JSONDetails
from Products.TinyMCE.adapters.interfaces.JSONDetails import IJSONDetails
from Products.TinyMCE.interfaces.utility import ITinyMCE


def getDetails(self):
    """Builds a JSON object based on the details
       of this object.
    """

    utility = getUtility(ITinyMCE)
    anchor_portal_types = utility.containsanchors.split('\n')
    image_portal_types = utility.imageobjects.split('\n')

    results = {}
    results['title'] = self.context.title_or_id()
    results['description'] = self.context.Description()
    if self.context.portal_type in image_portal_types:
        if IPhoto.providedBy(self.context):
            image_field = self.context.getField('photo')
            results['owner'] = self.context.owner_name
            results['date_y'] = self.context.year
            results['date_m'] = self.context.month
            results['date_d'] = self.context.day
        else:
            image_field = self.context.getField('image')
        results['thumb'] = self.context.absolute_url() + "/image_thumb"
        
        results['scales'] = utility.getImageScales(image_field,
                                                   context=self.context)
    else:
        results['thumb'] = ""
    
    if self.context.portal_type in anchor_portal_types:
        results['anchors'] = []
        tree = HTMLTreeBuilder.TreeBuilder()
        tree.feed('<root>%s</root>' % self.context.getPrimaryField().getAccessor(self.context)())
        rootnode = tree.close()
        for x in rootnode.getiterator():
            if x.tag == "a":
                if "name" in x.keys():
                    results['anchors'].append(x.attrib['name'])
    else:
        results['anchors'] = []
    
    return json.dumps(results)

JSONDetails.getDetails = getDetails


from plone.app.imaging.scaling import *


class PhotoScaling(ImageScaling):
    """ view used for generating (and storing) image scales """
    
    def fieldname(self, fieldname):
        if fieldname == 'image':
            fieldname = 'photo'
        return fieldname

    def traverse(self, name, furtherPath):
        """ used for path traversal, i.e. in zope page templates """
        name = self.fieldname(name)
        if not furtherPath:
            field = self.context.getField(name)
            return field.get(self.context).tag()
        image = self.scale(name, furtherPath.pop())
        if image is not None:
            return image.tag()
        raise TraversalError(self, name)

    def field(self, fieldname):
        """ return the field for a given name """
        fieldname = self.fieldname(fieldname)
        if fieldname:
            return self.context.getField(fieldname)
        else:
            return self.context.getPrimaryField()

    def tag(self, fieldname=None, scale=None, **kwargs):
        fieldname = self.fieldname(fieldname)
        scale = self.scale(fieldname, scale)
        return scale.tag(**kwargs)
