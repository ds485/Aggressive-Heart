__author__ = 'ds'

import org__POA.asam.ods as ods_POA
import InstanceElement


class Measurement_i (ods_POA.Measurement, InstanceElement.InstanceElement_i):
    def __init__(self, instance):
        self.instance = instance.instance
        self.db = instance.db

    def createSMatLink(self):
        return

    def getSMatLinks(self):
        return

    def getValueMatrix(self):
        return

    def getValueMatrixInMode(self):
        return

    def removeSMatLink(self):
        return