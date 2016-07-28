import codecs

from os import path
from setuptools import find_packages, setup


def read(*parts):
    filename = path.join(path.dirname(__file__), *parts)
    with codecs.open(filename, encoding="utf-8") as fp:
        return fp.read()


setup(
    author="Pinax Team",
    author_email="team@pinaxproject.com",
    description="web analytics and metrics integration for Django",
    name="pinax-webanalytics",
    long_description=read("README.rst"),
    version="2.0.3",
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
    test_suite="runtests.runtests",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False
)
