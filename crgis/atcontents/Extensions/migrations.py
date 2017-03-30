
from Products.contentmigration.archetypes import InplaceATItemMigrator
from Products.contentmigration.walker import CustomQueryWalker

from transaction import savepoint
from Products.CMFCore.utils import getToolByName


def getMigrationWalker(context, migrator):
    """ set up migration walker using the given item migrator """
    portal = getToolByName(context, 'portal_url').getPortalObject()
    return CustomQueryWalker(portal, migrator, use_savepoint=False)


class DeitiesToTempleMigrator(InplaceATItemMigrator):
    src_portal_type = 'Deities'
    src_meta_type = 'Deities'
    dst_portal_type = 'Temple'
    dst_meta_type = 'Temple'
    
    def last_migrate_reindex(self):
        self.new.reindexObject(idxs=['object_provides', 'portal_type',
            'Type', 'UID'])


def getDeitiesToTempleMigrationWalker(self):
    return getMigrationWalker(self, migrator=DeitiesToTempleMigrator)


def migrateDeities(self):
    walker = getDeitiesToTempleMigrationWalker(self)
    savepoint(optimistic=True)
    walker.go()
    return walker.getOutput()
