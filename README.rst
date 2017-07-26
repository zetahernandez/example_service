Example Service
===============

This is meant to serve as an example of how to best write a service and handle
a variety of different patterns. All code is thoroughly commented, and suitable
for copying to base a new service on.

Any service you make should have a README like this that briefly describes what's
included in the service and how to work with it. More detailed documentation for
the service should be in the ``docs/`` directory, which must contain at least
``index.rst``. See https://docs.evbhome.com/repos/docs-in-repos.html for more info.


Things to include in the README
-------------------------------

Purpose
+++++++

* What is this service in charge of and what questions does it answer?


Maintainer
++++++++++

* Which team maintains this service?


Dependencies
++++++++++++

* What external dependencies does this service have? One possible audience for this
  is Ops, but this is also important for future maintainers and developers.
  Examples might be "core MySQL database", "Kafka", or "core Cassandra"


Developing for this service locally (Getting Started)
+++++++++++++++++++++++++++++++++++++++++++++++++++++

* General guidelines for working on the service
* Is there a specific core container to use?
* Is there a recommended profile?
* Any gotchas, common errors, or pitfalls?


How to Run Tests for this Service
+++++++++++++++++++++++++++++++++

* Running all tests
* Running a specific test


Release and Versioning
+++++++++++++++++++++++++++++++++++

* Instructions on releasing this service standalone
* Instructions on managing service as a library to install in core
* Additional deployment steps if this service is remote


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
    docs/
        index.rst
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
