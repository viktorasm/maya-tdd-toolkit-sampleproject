import unittest
from maya import cmds

class Test(unittest.TestCase):
    def testMinimal(self):
        '''
        do something with maya.cmds to prove we're actually running this test in Maya.
        '''
        cmds.sphere()
        

