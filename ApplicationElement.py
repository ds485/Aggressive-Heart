__author__ = 'ds'

import org__POA.asam.ods as ods_POA
import dbHandler
import ApplicationStructure
import InstanceElement
import BaseElement
import ConfigParser


class ApplicationElement_i (ods_POA.ApplicationElement):
    def __init__(self, name):
        self.name = name.lower()
        self.__mimetype = None
        self.__db = None
        self.__base = None
        self.__rels = None
        return

    def __get_rels(self):
        if self.__rels is None:
            self.__rels = self.__get_conf_elem("Rel")
        return self.__rels

    def __get_conf_elem(self, name):
        cp = ConfigParser.ConfigParser()
        cp.read("etc/ApplicationModel.conf")
        if cp.has_section(self.name):
            if cp.has_option(self.name, name):
                return cp.get(self.name, name)
        else:
            print "kein base fuer ", self.name, " gefunden"
            # TODO: raise some error

    def __get_db(self):
        if self.__db is None:
            self.__db = dbHandler.get_db()
        return self.__db

    def __get_base(self):
        if self.__base is None:
            self.__base = self.__get_conf_elem("Base")
        return self.__base

    def __get_mimetype(self):
        if self.__mimetype is None:
            base = self.__get_base()
            self.__mimetype = "application/x-asam." + base.lower() + "." + self.name
        return self.__mimetype

    def createAttribute(self):
        return

    def createInstance(self, name):
        db = self.__get_db()
        mimetype = self.__get_mimetype()
        instance = {"name": name, "mime_type": mimetype}
        db[self.name].insert(instance)
        ie = InstanceElement.InstanceElement_i(instance)
        return ie._this()

    def getAllRelatedElements(self):
        rels = self.__get_rels()
        aes = []
        if rels is not None:
            for rel in rels.split(","):
                rel = rel.strip()
                aes.append(ApplicationElement_i(rel)._this())
        return aes

    def getAllRelations(self):
        return

    def getAttributeByBaseName(self):
        return

    def getAttributeByName(self):
        return

    def getAttributes(self):
        return

    def getBaseElement(self):
        base = self.__get_base()
        be = BaseElement.BaseElement_i(base)
        return be._this()

    def getId(self):
        # TODO: raise not imple
        return

    def getInstanceById(self):
        # TODO: raise not imple
        return

    def getInstanceByName(self, name):
        db = self.__get_db()
        instance = db[self.name].find_one({"name": name})
        ie = InstanceElement.InstanceElement_i(instance)
        return ie._this()

    def getInstances(self):
        return

    def getName(self):
        return str(self.name)

    def getRelatedElementsByRelationship(self):
        return

    def getRelationsByType(self):
        return

    def listAllRelatedElements(self):
        return

    def listAttributes(self):
        return

    def listInstances(self):
        return

    def listRelatedElementsByRelationship(self):
        return

    def removeAttribute(self):
        return

    def removeInstance(self):
        return

    def setBaseElement(self):
        return

    def setName(self):
        return

    def setRights(self):
        return

    def getRights(self):
        return

    def getInitialRights(self):
        return

    def setInitialRights(self):
        return

    def setInitialRightRelation(self):
        return

    def getInitialRightRelations(self):
        return

    def getSecurityLevel(self):
        return

    def setSecurityLevel(self):
        return

    def getApplicationStructure(self):
        appstruct = ApplicationStructure.ApplicationStructure_i()
        return appstruct._this()

    def createInstances(self):
        return

    def getRelationsByBaseName(self):
        return