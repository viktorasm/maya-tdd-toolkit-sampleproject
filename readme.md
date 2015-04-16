# Maya TDD setup - sample project

This is a sample project that is using [maya-tdd-toolkit](https://github.com/viktorasm/maya-tdd-toolkit) for running tests inside Maya.

## how it works

It's pretty simple. Once Maya is launched, it starts listening for test launches.
While external test runner is running tests, they are instead instanced inside Maya and executed there; test result
is translated back to original test runner.

## basic setup

Once everything is working, the workflow is like this:

* Launch Maya with `./launch_maya.py` (preferably from your IDE, so you can get the output in there)
* Launch tests like usual from IDE.

## launch_maya.py

This file is where you configure how to tailor Maya configuration to running tests in your project.

## sampleproject_tests/setup.py

A special file that will need to be introduced at the root test package; test runner requires slight configuration, so it's automagically discovered in that file.

## testMayaLaunchEnvironment

When Maya gets launched, a copy of this folder will be created to be used as Maya home dir. Don't version-control the copy,
but definitely include this one, and update as needed to have Maya configured just the way you want it for tests. In this project's case, we've disabled all plugins. 

The folder now only contains a setup for 2015 maya, should be enough to illustrate idea.