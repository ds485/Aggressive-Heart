__author__ = 'ds'

import org__POA.asam.ods as ods_POA
import dbHandler
import ApplicationElement


class InstanceElement_i(ods_POA.InstanceElement):

    def __init__(self, instance):
        self.db = dbHandler.get_db()
        self.instance = instance

    def addInstanceAttribute(self):
        return

    def createRelation(self):
        return

    def getApplicationElement(self):
        name = self.instance["mime_type"].split(".")[2]
        ae_i = ApplicationElement.ApplicationElement_i(name)
        return ae_i._this()

    def getAsamPath(self):
        return

    def getId(self):
        return

    def getName(self):
        return str(self.instance["name"])

    def getRelatedInstances(self):
        return

    def getRelatedInstancesByRelationship(self):
        return

    def getValue(self):
        return

    def getValueByBaseName(self):
        return

    def listAttributes(self):
        return

    def listRelatedInstances(self):
        return

    def listRelatedInstancesByRelationship(self):
        return

    def removeInstanceAttribute(self):
        return

    def removeRelation(self):
        return

    def renameInstanceAttribute(self):
        return

    def setName(self):
        return

    def setValue(self):
        return

    def upcastMeasurement(self):
        # TODO: muss noch gecheckt werden das es auf der instanz erlaubt ist
        import Measurement
        mea = Measurement.Measurement_i(self)
        return mea._this()

    def upcastSubMatrix(self):
        # TODO: muss noch gecheckt werden das es auf der instanz erlaubt ist
        import SubMatrix
        mea = SubMatrix.SubMatrix_i(self)
        return mea._this()

    def getValueInUnit(self):
        return

    def setValueSeq(self):
        return

    def setRights(self):
        return

    def getRights(self):
        return

    def getInitialRights(self):
        return

    def setInitialRights(self):
        return

    def shallowCopy(self):
        return

    def deepCopy(self):
        return

    def getValueSeq(self):
        return

    def destroy(self):
        return

    def compare(self):
        return

    def createRelatedInstances(self):
        return