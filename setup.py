from setuptools import (
    find_packages,
    setup,
)

from example_service import __version__


def readme():
    with open('README.rst') as f:
        return f.read()


# Put your requirements for installation here. Try to use the ~= operator where possible for dependencies, which will
# allow bug fix releases in that branch. For example, "conformity~=1.12" allows anything up to but not including 2.0,
# while "pysoa~=0.38.1" allows anything up to but not including 0.39.0.
install_requires = [
    'pysoa~=0.38.1',
    'conformity~=1.12',
]

# Extra requirements that are needed for running tests but NOT for running in production should go here.
tests_require = [
    'pytest',
    'pytest-cov',
]


setup(
    name='example_service',
    version=__version__,
    author='Eventbrite, Inc.',
    author_email='opensource@eventbrite.com',
    description='A short one-line service description goes here.',
    long_description=readme(),
    url='https://github.com/eventbrite/example_service',
    packages=find_packages(exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),
    include_package_data=True,
    install_requires=install_requires,
    tests_require=tests_require,
    setup_requires=['pytest-runner'],
    test_suite='tests',
    extras_require={
        'testing': tests_require,
    },
    # This tells Python to install an "example_service" binary on the system that calls the Server.main() function,
    # which runs the server - meaning you can just type "example_service" on the command line once this is installed
    # in order to run it.
    entry_points={
        'console_scripts': [
            'example_service=example_service.standalone:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development',
    ],
)
