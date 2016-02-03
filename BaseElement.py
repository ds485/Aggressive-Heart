__author__ = 'ds'

import org__POA.asam.ods as ods_POA


class BaseElement_i (ods_POA.BaseElement):
    def __init__(self, base):
        self.base = base

    def getAllRelations(self):
        return

    def getAttributes(self):
        return

    def getRelatedElementsByRelationship(self):
        return

    def getRelationsByType(self):
        return

    def getType(self):
        return str(self.base)

    def isTopLevel(self):
        return

    def listAttributes(self):
        return

    def listRelatedElementsByRelationship(self):
        return