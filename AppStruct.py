__author__ = 'ds'


appstruct = None


def get_app_struct():
    global appstruct
    if appstruct is not None:
        return appstruct
    appstruct = AppStruct()
    return appstruct


class AppStruct():

    def __init__(self):
        self.user = None

    def set_aouser(self, user):
        self.user = user
        if not self.__check_aouser():
            print "aouser is nicht"

    def __check_aouser(self):
        collections = self.db.collection_names()
        if self.aouser in collections:
            True
        False