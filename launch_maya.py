from mayatdd.launchMaya import Launcher
from os import path
 
# discover root dir of our project
projectRoot = path.dirname(__file__)

launcher = Launcher()
launcher.mayaEnvTemplateDir = path.abspath(path.join(projectRoot,'testMayaLaunchEnvironment'))

# specific options for windows?
if launcher.isWindows:
    launcher.mayaExecutable = r'C:\Program Files\Autodesk\Maya2015\bin\maya.exe'

launcher.launch() 

