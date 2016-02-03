__author__ = 'ds'

import org__POA.asam.ods as ods_POA
import ApplicationElement


class ApplicationStructure_i (ods_POA.ApplicationStructure):
    def __init__(self):
        return

    def check(self):
        return

    def createElement(self):
        return

    def createRelation(self):
        return

    def getElementById(self):
        return

    def getElementByName(self, name):
        ae_i = ApplicationElement.ApplicationElement_i(name)
        return ae_i._this()

    def getElements(self):
        return

    def getElementsByBaseType(self):
        return

    def getInstanceByAsamPath(self):
        return

    def getRelations(self):
        return

    def getTopLevelElements(self):
        return

    def listElements(self):
        return

    def listElementsByBaseType(self):
        return

    def listTopLevelElements(self):
        return

    def removeElement(self):
        return

    def removeRelation(self):
        return

    def getInstancesById(self):
        return

    def getSession(self):
        return

    def createEnumerationDefinition(self):
        return

    def removeEnumerationDefinition(self):
        return

    def listEnumerations(self):
        return

    def getEnumerationDefinition(self):
        return

    def createInstanceRelations(self):
        return