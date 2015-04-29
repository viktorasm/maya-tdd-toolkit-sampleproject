# Maya TDD setup - sample project

This is a sample project that is using [maya-tdd-toolkit](https://github.com/viktorasm/maya-tdd-toolkit) for running tests inside Maya.

## how it works

It's pretty simple. Once Maya is launched, it starts listening for test launches.
While external test runner is running tests, they are instead instanced inside Maya and executed there; test result
is translated back to original test runner.

## basic setup

Once everything is working, the workflow will be like this:

* Launch Maya with `./launch_maya.py` (preferably from your IDE, so you can get the output in there)
* Launch tests like usual from IDE or command line

## quick start

Clone project, setup virtual environment and install all required libs:

```bash
git clone https://github.com/viktorasm/maya-tdd-toolkit-sampleproject.git
cd maya-tdd-toolkit-sampleproject
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
#launch maya and wait while it finishes initializing (or run the equivalend command in your IDE)
venv/bin/python launch_maya.py &
# run tests
nosetests -v
```




## launch_maya.py

This file is where you configure how to tailor Maya configuration to running tests in your project.

## sampleproject_tests/__init__.py

See details of this file - some options need to be tailored for your project, along with optional startup hooks.

## testMayaLaunchEnvironment

When Maya gets launched, a copy of this folder will be created to be used as Maya home dir. Don't version-control the copy,
but definitely include this one, and update as needed to have Maya configured just the way you want it for tests. In this project's case, we've disabled all plugins. 

The folder now only contains a setup for 2015 maya, should be enough to illustrate idea.