# Maya TDD setup - sample project

This is a sample project that is using [maya-tdd-toolkit](https://github.com/viktorasm/maya-tdd-toolkit) for running tests inside Maya.

## basic setup
Once everything is working, the workflow is like this:

* Launch Maya with `./launch_maya.py` (preferably from your IDE, so you can get the output in there)
* Launch tests with `./launch_tests.py` (also from IDE)

## launch_maya.py

This file is where you configure how to tailor Maya configuration to running tests in your project.

## launch_tests.py

Just a shortcut in your project to understand how to launch test suite.

## sampleproject_tests/setup.py

A special file that will need to be introduced at the root test package; test runner requires slight configuration, so it's automagically discovered in that file.

## testMayaLaunchEnvironment

When maya gets launched, a copy of this folder will be created to be used as Maya home dir. Don't version-control the copy,
but keep a copy of this one, and update as needed to have Maya configured just the way you want it for tests. In this projects case, we've just disabled all plugins, for example. 

The folder now only contains a setup for 2015 maya, should be enough to illustrate idea.