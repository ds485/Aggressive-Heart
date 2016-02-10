__author__ = 'ds'

import sys
from omniORB import CORBA
import org.asam.ods as ods


def print_rels(aes):
    for ae in aes:
        print "ae name: ", ae.getName()
        print "ae type: ", ae.getBaseElement().getType()
        print_rels(ae.getAllRelatedElements())

user = "user"
pw = "pass"
auth = "USER=%s,PASSWORD=%s,CREATE_COSESSION_ALLOWED=FALSE" % (user, pw)

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)

ior = sys.argv[1]
obj = orb.string_to_object(ior)

eo = obj._narrow(ods.AoFactory)
if eo is None:
    print "Object reference is not an AoFactory"
    sys.exit(1)

print "desc: ", eo.getDescription()
print "version: ", eo.getInterfaceVersion()
print "name: ", eo.getName()
print "type: ", eo.getType()
print "------"

session = eo.newSession(auth)
if session is None:
    print "no session"
    sys.exit(1)

user = session.getUser()
appstruct = session.getApplicationStructure()

if appstruct is None:
    print "no as"
    sys.exit(1)

ae = appstruct.getElementByName("Project")
print "ae name: ", ae.getName()

ie = ae.getInstanceByName("pro3")
print "ie name: ", ie.getName()
print "----------"

i = 0
while i < 1:
    ae = ie.getApplicationElement()
    ie = ae.getInstanceByName("pro3")
    i += 1


ae = appstruct.getElementByName("mearesult")
ie = ae.getInstanceByName("mea1")

print "------------------"
print "ie name: ", ie.getName()
print dir(ie)
print type(ie)

mea = ie.upcastMeasurement()

print "------------------"
print dir(mea)
print type(mea)
print "mea name: ", mea.getName()


print "ae base: ", ie.getApplicationElement().getBaseElement().getType()
aes = ae.getAllRelatedElements()
print_rels(aes)
