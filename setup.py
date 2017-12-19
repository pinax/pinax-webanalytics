from setuptools import find_packages, setup

LONG_DESCRIPTION = """
.. image:: http://pinaxproject.com/pinax-design/patches/pinax-blank.svg
    :target: https://pypi.python.org/pypi/pinax-webanalytics/
===================
Pinax Notifications
===================
.. image:: https://img.shields.io/pypi/v/pinax-webanalytics.svg
    :target: https://pypi.python.org/pypi/pinax-webanalytics/
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://pypi.python.org/pypi/pinax-webanalytics/
.. image:: https://img.shields.io/circleci/project/github/pinax/pinax-webanalytics.svg
    :target: https://circleci.com/gh/pinax/pinax-webanalytics
.. image:: https://img.shields.io/codecov/c/github/pinax/pinax-webanalytics.svg
    :target: https://codecov.io/gh/pinax/pinax-webanalytics
.. image:: https://img.shields.io/github/contributors/pinax/pinax-webanalytics.svg
    :target: https://github.com/pinax/pinax-webanalytics/graphs/contributors
.. image:: https://img.shields.io/github/issues-pr/pinax/pinax-webanalytics.svg
    :target: https://github.com/pinax/pinax-webanalytics/pulls
.. image:: https://img.shields.io/github/issues-pr-closed/pinax/pinax-webanalytics.svg
    :target: https://github.com/pinax/pinax-webanalytics/pulls?q=is%3Apr+is%3Aclosed
.. image:: http://slack.pinaxproject.com/badge.svg
    :target: http://slack.pinaxproject.com/

``pinax-webanalytics`` provides analytics and metrics integration for Django.
 
``pinax-app`` does this and that.

Features
--------
* Good helpful stuff 

Supported Django and Python Versions
------------------------------------
+-----------------+-----+-----+-----+-----+
| Django \ Python | 2.7 | 3.4 | 3.5 | 3.6 |
+=================+=====+=====+=====+=====+
| 1.11            |  *  |  *  |  *  |  *  |
+-----------------+-----+-----+-----+-----+
| 2.0             |     |  *  |  *  |  *  |
+-----------------+-----+-----+-----+-----+
"""

setup(
    author="Pinax Team",
    author_email="team@pinaxproject.com",
    description="web analytics and metrics integration for Django",
    name="pinax-webanalytics",
    long_description=LONG_DESCRIPTION,
    version="4.0.0",
    url="http://github.com/pinax/pinax-webanalytics",
    license="MIT",
    packages=find_packages(),
    package_data={
        "pinax.webanalytics": [
            "templates/pinax/webanalytics/_adwords_conversion.html",
            "templates/pinax/webanalytics/_gauges.html",
            "templates/pinax/webanalytics/_google.html",
            "templates/pinax/webanalytics/_mixpanel.html",
        ]
    },
    install_requires=[
    ],
    test_suite="runtests.runtests",
    tests_require=[
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False
)
