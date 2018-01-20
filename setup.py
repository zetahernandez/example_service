from setuptools import (
    find_packages,
    setup,
)

from example_service import __version__


# Put your requirements for installation here. Try to use the ~= operator where possible for dependencies, which will
# allow bug fix releases in that branch. For example, "conformity~=1.6" allows anything up to but not including 2.0.
install_requires = [
    'pysoa~=0.26.1',
    'conformity~=1.7',
]

# Extra requirements that are needed for running tests but NOT for running in production should go here.
tests_require = [
    'pytest',
    'pytest-cov',
]


setup(
    name='example_service',
    description='A short one-line service description goes here.',
    version=__version__,
    packages=find_packages(),
    install_requires=install_requires,
    tests_require=tests_require,
    setup_requires=['pytest-runner'],
    extras_require={
        'testing': tests_require,
    },
    # This tells Python to install an "example_service" binary on the system that calls the Server.main() function,
    # which runs the server - meaning you can just type "example_service" on the command line once this is installed
    # in order to run it.
    entry_points={
        'console_scripts': [
            'example_service=example_service.standalone:main',
        ]
    },
)
