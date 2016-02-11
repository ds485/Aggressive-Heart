__author__ = 'ds'

import sys
from omniORB import CORBA, PortableServer
import AoFactory
import ConfigParser
import CosNaming
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

obj = orb.resolve_initial_references("NameService")
cxt = obj._narrow(CosNaming.NamingContext)

name = [CosNaming.NameComponent("test", "my_context")]
try:
    testContext = cxt.bind_new_context(name)
    print "New test context bound"
except CosNaming.NamingContext.AlreadyBound, ex:
    print "Test context already exists"
    obj = cxt.resolve(name)
    testContext = obj._narrow(CosNaming.NamingContext)
    if testContext is None:
        print "test.mycontext exists but is not a NamingContext"
        sys.exit(1)


aofi = AoFactory.AoFactory_i()
aofo = aofi._this()


name = [CosNaming.NameComponent("AoFactory", "Object")]
try:
    testContext.bind(name, aofo)
    print "New AoFactory object bound"
except CosNaming.NamingContext.AlreadyBound:
    testContext.rebind(name, aofo)
    print "AoFactory binding already existed -- rebound"


# print orb.object_to_string(aofo)

poaManager = poa._get_the_POAManager()
poaManager.activate()

orb.run()
