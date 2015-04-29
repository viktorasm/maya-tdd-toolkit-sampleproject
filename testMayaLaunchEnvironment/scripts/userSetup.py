import sys
import os

# remove installed ngSkinTools if present in path
for i in sys.path[:]:
    if 'ngSkinTools' in i:
        sys.path.remove(i)

if os.environ.has_key('maya_test_pythonpath'):
    for i in os.environ['maya_test_pythonpath'].split(";"):
        print "adding test path:",i
        sys.path.append(i)

from ngst_testsupport import reloader
reload(reloader)
reloader.unload()


import dccautomation
from dccautomation import configs as dcconf

dccautomation.start_inproc_server(dcconf.Maya2015OSX(), 9025)

