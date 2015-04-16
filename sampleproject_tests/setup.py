# all modules prefixed with these package names will get reloaded before test execution
# in this case, sampleproject.* and sampleproject_tests.* will be reloaded
# based on below setting  
reloadModules = ['sampleproject']

# sysPath array defines additional directories to be added to Maya's classpath when executing tests.
# usually that's at least your project root folder
from os.path import dirname
sysPath = [dirname(dirname(__file__))]

# create a shortcut to mayaTest(setupModule) decorator to be used to decorate our tests
import mayatdd.mayatest
mayaTest = mayatdd.mayatest.mayaTest(__name__)