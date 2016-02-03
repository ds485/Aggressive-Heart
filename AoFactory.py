__author__ = 'ds'

import org__POA.asam.ods as ods_POA
import dbHandler
import AoSession


class AoFactory_i (ods_POA.AoFactory):

    def __init__(self):
        self.db = dbHandler.get_db()
        self.env = None

    def __get_env(self):
        if self.env is None:
            self.env = self.db.AoEnvironment.find_one({"mime_type": 'application/x-asam.aoenvironment'})
        return self.env

    def getDescription(self):
        env = self.__get_env()
        return str(env["description"])

    def getInterfaceVersion(self):
        return "V5.2.0"

    def getName(self):
        return "AoFactoryName"

    def getType(self):
        env = self.__get_env()
        try:
            return str(env["application_model_type"])
        except KeyError:
            return ""

    def newSession(self, auth):
        from parse import parse
        user, password, cosession = parse("USER={},PASSWORD={},CREATE_COSESSION_ALLOWED={}", auth)
        if self.db.AoUser.find_one({"mime_type": 'application/x-asam.aouser', "name": user, "password": password}):
            session_i = AoSession.AoSession_i(self.getName(), auth)
            session = session_i._this()
            return session
        # else:
        # TODO: raise AoException AO_CONNECT_FAILED