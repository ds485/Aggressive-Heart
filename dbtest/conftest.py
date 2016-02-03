__author__ = 'ds'

import ConfigParser





cp = ConfigParser.ConfigParser()
name = "Project"
# cp.read("fts.conf")

#cp.optionxform = str
cp.read("ApplicationModel.conf")
print cp.sections()
if cp.has_section(name):
    if cp.has_option(name, "base"):
        print cp.get(name, "base")


# secs = cp.sections()
# for sec in secs:
#     if cp.has_option(sec, "aouser"):
#         user = cp.get(sec, "aouser")
#         if not user:
#             print "no aouser def"
#         else:
#             print ":", user, ":"
#     else:
#         print "no aouser def"
