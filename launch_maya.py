from mayatdd.launchMaya import Launcher
from os import path
 
# discover root dir of our project
projectRoot = path.dirname(__file__)

launcher = Launcher()
launcher.mayaEnvTemplateDir = projectRoot+'/testMayaLaunchEnvironment'

# configure python path; for our project, we need to add root folder of this project
# depending on what kind of project layout you have, or what kind of libraries you use,
# you might need more entries here 
launcher.pythonPath.append(projectRoot)
# you'll need to have dccautomation project checked out somewhere,
# for me it's just outside my workspace (
launcher.pythonPath.append(path.abspath(projectRoot+r'/../../dccautomation'))

# specific options for windows?
if launcher.isWindows:
    launcher.mayaExecutable = r'C:\Program Files\Autodesk\Maya2015\bin\maya.exe'

launcher.launch() 

