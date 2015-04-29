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


def cleanUp():
    '''
    this optional method gets called before tests get executed, BEOFRE reloading newest code.
    use it to do any cleanup before your cached classes and global variables get thrown away.
    '''
    
    print "hi maya, about to clean up!"
    
    

def setup():
    '''
    this method gets called before tests get executed, after reloading newest code
    '''
    
    print "hi maya, we're ready to go!"
    
    