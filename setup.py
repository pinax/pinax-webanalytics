import codecs

from os import path
from setuptools import find_packages, setup


def read(*parts):
    filename = path.join(path.dirname(__file__), *parts)
    with codecs.open(filename, encoding="utf-8") as fp:
        return fp.read()


PACKAGE = "metron"
NAME = "metron"
DESCRIPTION = "analytics and metrics integration for Django"
AUTHOR = "Pinax Team"
AUTHOR_EMAIL = "team@pinaxproject.com"
URL = "http://github.com/pinax/metron"


setup(
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    name=PACKAGE,
    long_description=read("README.rst"),
    version="1.3.6",
    url="http://metron.rtfd.org/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "metron": [
            "templates/metron/_adwords_conversion.html",
            "templates/metron/_gauges.html",
            "templates/metron/_google.html",
            "templates/metron/_mixpanel.html",
        ]
    },
    test_suite="runtests.runtests",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2"
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False
)
