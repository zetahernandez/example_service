Example Service
===============

This is meant to serve as an example of how to best write a service and handle
a variety of different patterns. All code is thoroughly commented, and suitable
for copying to base a new service on.

Any service you make should have a README like this that says what the service
does, who maintains it, and what external dependencies (e.g. "core mysql database",
"kafka", "core cassandra") that service has so that Ops can know what to allow
it to access.


Maintainer
----------

The example service is maintained by the Foundry team.


Dependencies
------------

The example service has no external dependencies.


Folder Layout
-------------

All services should have their Python code in the top-level, with a ``setup.py``
file, a README file, and the service package directly in that top level folder,
like this::

    setup.py
    README.rst
    example_service/
        __init__.py
        server.py
        ...
    tests/
        ...
    scripts/
        jenkins_build.sh

Don't put the code in a ``python/`` subfolder or similar.


Building
--------

Your service should have a script called ``scripts/jenkins_build.sh`` that
can be run by Jenkins and produces a tar.gz file of the code that is ready to
deploy. For more on how this works, see the included example.

The Docker build instructions for our dev environment will live in the
``docker-dev`` repo, separately.


Testing
-------

Use ``python setup.py test`` to run tests. Use py.test; do not use nosetests,
as it's now deprecated and unmaintained.

The setup.py file contained here uses py.test to run tests located in a
``tests/`` directory.
