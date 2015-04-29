import unittest
from sampleproject_tests import mayaTest
from mayatdd.mayatest import insideMaya
if insideMaya:
    from maya import cmds

@mayaTest
class Test(unittest.TestCase):
    def testMinimal(self):
        '''
        do something with maya.cmds to prove we're actually running this test in Maya.
        '''
        cmds.sphere()
        

