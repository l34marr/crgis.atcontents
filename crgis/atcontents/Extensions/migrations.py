#!/usr/bin/python
# -*- coding: utf-8 -*-

from Products.contentmigration.archetypes import InplaceATItemMigrator, ATItemMigrator
from Products.contentmigration.walker import CustomQueryWalker
from Products.contentmigration.archetypes import *
from Products.contentmigration.common import unrestricted_rename

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

    fields_map = {
        'temple_code': 'code',
        'templesource': 'data_src',
        'other_0': 'data_src_o',
        'coordinate_resource': 'coordinate',
        'other_00': 'coordinate_o',
        'direction_s': 'facing',
        'deity_name': 'deity_host',
        'deity_name_other': 'deity_host_o',
        'deity_title': 'deity_host_a',
        'other_01': 'religion_o',
        'temple_type': 'building',
        'other_02': 'building_o',
        'english_era': 'era',
        'china_era_1': 'era_1',
        'china_era_2': 'era_2',
        'china_era': 'era_ref',
        'construct': 'funding',
        'other_03': 'funding_o',
        'organize': 'organizing',
        'other_04': 'organizing_o',
        'promoter': 'in_charge',
        'deities_accompany': 'deity_accompany',
        'ceremony_action': 'worship',
        'temple_introduction': 'introduction',
        'temple_condition': 'overview',
        'edu_wediting': 'academic',
        'study_book': 'literature',
        'enterer': 'fill_in',
        'lastupdate': 'fill_date',
        'jstq_other': 'jstq_o',
        'flxt_other': 'flxt_o',
        'ymmy_other': 'ymmy_o',
        'xhly_other': 'xhly_o',
        'nlqs_other': 'nlqs_o',
        'wyxx_other': 'wyxx_o',
        'desc_other': 'desc_o',
    }

def getDeitiesToTempleMigrationWalker(self):
    return getMigrationWalker(self, migrator=DeitiesToTempleMigrator)


def migrateDeities(self):
    walker = getDeitiesToTempleMigrationWalker(self)
    savepoint(optimistic=True)
    walker.go()
    return walker.getOutput()


class ImagesToPhotosMigrator(InplaceATItemMigrator):
    src_portal_type = 'Image'
    src_meta_type = 'ATBlob'
    dst_portal_type = 'Photo'
    dst_meta_type = 'Photo'
    
    def last_migrate_reindex(self):
        self.new.reindexObject(idxs=['object_provides', 'portal_type',
            'Type', 'UID'])
    
    fields_map = {
    }

def getImagesToPhotosMigrationWalker(self):
    return getMigrationWalker(self, migrator=ImagesToPhotosMigrator)

def migrateImages(self):
    walker = getImagesToPhotosMigrationWalker(self, {'path': '/temple'})
    #savepoint(optimistic=False)
    walker.go()
    return walker.getOutput()

