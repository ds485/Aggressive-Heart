__author__ = 'ds'

import org__POA.asam.ods as ods_POA
from parse import parse
import InstanceElement
import ApplicationStructure
import dbHandler


class AoSession_i (ods_POA.AoSession):

    def __init__(self, name, auth):
        self.db = dbHandler.get_db()
        self.name = name
        self.user, self.password, self.cosession = parse("USER={},PASSWORD={},CREATE_COSESSION_ALLOWED={}", auth)

    def abortTransaction(self):
        return

    def close(self):
        return

    def commitTransaction(self):
        return

    def getApplicationStructure(self):
        appstruct_i = ApplicationStructure.ApplicationStructure_i()
        return appstruct_i._this()

    def getApplicationStructureValue(self):
        return

    def getBaseStructure(self):
        return

    def getContext(self, Pattern):
        return

    def getContextByName(self, Name):
        return

    def listContext(self, Pattern):
        return

    def removeContext(self, Pattern):
        return

    def setContext(self, contextVariable):
        return

    def setContextString(self, Name, value):
        return

    def startTransaction(self):
        return

    def flush(self):
        return

    def setCurrentInitialRights(self, irlEntries, set):
        return

    def getLockMode(self):
        return

    def setLockMode(self, lockMode):
        return

    def getApplElemAccess(self):
        return

    def setPassword(self, username, oldPassword, newPassword):
        return

    def getDescription(self):
        return

    def getName(self):
        return self.name

    def getType(self):
        return

    def createQueryEvaluator(self):
        return

    def createBlob(self):
        return

    def createCoSession(self):
        return

    def getUser(self):
        result = self.db.AoUser.find_one({"mime_type": 'application/x-asam.aouser', "name": self.user})
        ie_i = InstanceElement.InstanceElement_i(result)
        ie = ie_i._this()
        return ie

    def getEnumerationAttributes(self):
        return

    def getEnumerationStructure(self):
        return