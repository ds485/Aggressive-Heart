__author__ = 'ds'

import org__POA.asam.ods as ods_POA
import InstanceElement


class SubMatrix_i (ods_POA.SubMatrix, InstanceElement.InstanceElement_i):
    def __init__(self, instance):
        self.instance = instance.instance
        self.db = instance.db

    def getColumns(self):
        return

    def getValueMatrix(self):
        return

    def getValueMatrixInMode(self):
        return

    def listColumns(self):
        return