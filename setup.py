from distutils.core import setup

# see requirements.txt for dependencies



setup(
    name = "metron",
    version = "0.1.dev1",
    author = "Eldarion",
    author_email = "development@eldarion.com",
    description = "an app for managing analytics service integration",
    long_description = open("README.rst").read(),
    license = "BSD",
    url = "http://github.com/eldarion/metron",
    packages = [
        "metron",
        "metron.templatetags",
    ],
    package_data = {
        "biblion": [
            "templates/metron/*.html",
        ]
    },
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
