__author__ = 'ds'

import sys
from omniORB import CORBA, PortableServer
import AoFactory
import ConfigParser
import AppStruct


def read_config():
    cp = ConfigParser.ConfigParser()
    cp.read("etc/fts.conf")
    secs = cp.sections()
    for sec in secs:
        if cp.has_option(sec, "aouser"):
            aouser = cp.get(sec, "aouser")
            if aouser:
                return aouser
        print "no aouser def"
        # TODO: raise something
        return ""


# aouser = read_config()
# apps = AppStruct.get_app_struct()
# apps.set_aouser(aouser)

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
poa = orb.resolve_initial_references("RootPOA")

aofi = AoFactory.AoFactory_i()
aofo = aofi._this()

print orb.object_to_string(aofo)

poaManager = poa._get_the_POAManager()
poaManager.activate()

orb.run()