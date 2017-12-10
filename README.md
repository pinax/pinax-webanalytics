# Pinax Web Analytics

[![](https://img.shields.io/pypi/v/pinax-webanalytics.svg)](https://pypi.python.org/pypi/pinax-webanalytics/)

[![Codecov](https://img.shields.io/codecov/c/github/pinax/pinax-webanalytics.svg)](https://codecov.io/gh/pinax/pinax-webanalytics)
[![CircleCI](https://circleci.com/gh/pinax/pinax-webanalytics.svg?style=svg)](https://circleci.com/gh/pinax/pinax-webanalytics)
![](https://img.shields.io/github/contributors/pinax/pinax-webanalytics.svg)
![](https://img.shields.io/github/issues-pr/pinax/pinax-webanalytics.svg)
![](https://img.shields.io/github/issues-pr-closed/pinax/pinax-webanalytics.svg)

[![](http://slack.pinaxproject.com/badge.svg)](http://slack.pinaxproject.com/)
[![](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Table of Contents

* [About Pinax](#about-pinax)
* [Overview](#overview)
  * [Features](#features)
  * [Supported Django and Python versions](#supported-django-and-python-versions)
* [Documentation](#documentation)
  * [Installation](#installation)
  * [Settings](#settings)
  * [Templates](#templates)
  * [Usage](#usage)
* [Change Log](#change-log)
* [Contribute](#contribute)
* [Code of Conduct](#code-of-conduct)
* [Connect with Pinax](#connect-with-pinax)
* [License](#license)


# About Pinax

Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable Django apps, themes, and starter project templates.
This collection can be found at http://pinaxproject.com.

This app was developed as part of the Pinax ecosystem but is just a Django app and can be used independently of other Pinax apps.

## pinax-webanalytics

### Overview

``pinax-webanalytics`` provides analytics and metrics integration for Django.

Current analytics services supported:

* Google Analytics
* Mixpanel
* gaug.es
* Google AdWords Conversion Tracking

#### Supported Django and Python versions

Django \ Python | 2.7 | 3.4 | 3.5 | 3.6
--------------- | --- | --- | --- | ---
1.11 |  *  |  *  |  *  |  *  
2.0  |     |  *  |  *  |  *



## Documentation

### Installation

* To install `pinax-webanalytics`:

```
pip install pinax-webanalytics
```

* Add `pinax-webanalytics` to your `INSTALLED_APPS` setting::

```python
INSTALLED_APPS = (
    # other apps
    "pinax.webanalytics",
)
```

* See the list of [settings](#settings) to modify pinax-webanalytics's
  default behavior and make adjustments for your website.
  
  
### Settings

#### PINAX_WEBANALYTICS_ADWORDS_SETTINGS

This sets the conversion identifiers for AdWords for the conversions
you want to track indexed by page specific keys:

```python
PINAX_WEBANALYTICS_ADWORDS_SETTINGS = {
    "waitinglist": {
        "conversion_id": "",
        "conversion_label": "",
        "conversion_format": ""
    }
}
```

#### PINAX_WEBANALYTICS_SETTINGS

This is a data structure defining your analytics and metrics settings
indexed by `settings.SITE_ID` (or `request.pwa_site_id`.) Example:

```python
PINAX_WEBANALYTICS_SETTINGS = {
    "mixpanel": {
        1: "", # production
        2: "", # beta
    },
    "google": {
        1: "", # production
        2: "", # beta
    },
    "gauges": {
        1: "",
    }
}
```

where the values you would supply for each service and `SITE_ID` (or
`request.pwa_site_id`) node is the identifier code for that service.

Note that, as of 1.1, the site ID keys *must* be integers, not strings.

### Templates

pinax-webanalytics ships with templates for three services out of the box, gaug.es, Google
Analytics and Mixpanel. This can be overridden in your project for customizations
and likewise if there are other services you wish to use, just create a similar
template under the `pinax-webanalytics` folder in your templates directory. The format is
``"_%s.html" % slug`` where the slug is what index the `PINAX_WEBANALYTICS_SETTINGS` dict with.

#### `_gauges.html`

This snippet is used for gaug.es

#### `_google.html`

This snippet is used for Google Analytics

#### `_mixpanel.html`

This snippet is used for Mixpanel

#### `_adwords_conversion.html`

This snippet is used by the `adwords_conversion` template tag

### Usage

Integrating `pinax-webanalytics` quite simple::

```
    {% load pinax_webanalytics_tags %}
```

and then toward the bottom of the body where you put your scripts:

```
    {% analytics %}
```

If you want to add certain specific activities you can use the activity
API in `pinax-webanalytics` like so:

```python
from pinax.webanalytics import activity

activity.add(request, "mixpanel", "track", "Node Viewed", {
    "node": self.get_object().title,
    "user": request.user.username
})
```

You would typically want to call this within a view where you had some
activity you wanted to track that was more transactional than could be
determined by simply a certain page view.

The parameters for this are the request, the kind, then the method that
is used on the kind's javascript API, followed by a list of args that
will be passed to that javascript API.

#### AdWords Conversion Tracking

Load the template tags as above:

```
    {% load pinax_webanalytics_tags %}
```

then toward the bottom of the body, include:

```
    {% adwords_conversion "waitinglist" %}
```

where the argument passed to `adwords_conversion` is the key used in
`PINAX_WEBANALYTICS_ADWORDS_SETTINGS` to provide the conversion id, label and
format.


## ChangeLog

### 4.0.0

* Add Django 2.0 compatibility testing
* Drop Django 1.8, 1.9, 1.10 and Python 3.3 support
* Convert CI and coverage to CircleCi and CodeCov
* Add PyPi-compatible long description
* Move documentation to README.md

### 3.0.0

* use plain `dict` instead of `template.Context`

### 2.0.4

* updated this change log

### 2.0.3

* fixed typo in installation instructions

### 2.0.2

* corrected broken doc link in README

### 2.0.1

* fixed import path

### 2.0

* renamed to `pinax-webanalytics`

#### BI

* template fragments now reside in `pinax/webanalytics/`
* settings prefixes changed from `METRON_` to `PINAX_WEBANALYTICS_`
* `request.metron_site_id` changed to `request.pwa_site_id`, but still defaults to `settings.SITE_ID` if not on `request` object
* the session key name now defaults to `_pwa_activity` instead of `_metron_activity`

### 1.3

* site ID keys in METRON_SETTINGS can reference the value stored in
  ``request.metron_site_id`` (useful for multi-tenancy setups)

### 1.2

* Upgraded mixpanel

### 1.1

* ``SITE_ID`` is now always treated as an int on lookup so the keys in
  ``METRON_SETTINGS`` must be ints
* analytics template tag now bails out silently if ``user`` or ``request`` are
  missing from context

### 1.0

* same as 0.2

### 0.2

* added activity tracking
* added adwords conversion tracking (per page template tag)

### 0.1

* initial release


## Contribute

For an overview on how contributing to Pinax works read this [blog post](http://blog.pinaxproject.com/2016/02/26/recap-february-pinax-hangout/)
and watch the included video, or read our [How to Contribute](http://pinaxproject.com/pinax/how_to_contribute/) section.
For concrete contribution ideas, please see our
[Ways to Contribute/What We Need Help With](http://pinaxproject.com/pinax/ways_to_contribute/) section.

In case of any questions we recommend you join our [Pinax Slack team](http://slack.pinaxproject.com)
and ping us there instead of creating an issue on GitHub. Creating issues on GitHub is of course
also valid but we are usually able to help you faster if you ping us in Slack.

We also highly recommend reading our blog post on [Open Source and Self-Care](http://blog.pinaxproject.com/2016/01/19/open-source-and-self-care/).

## Code of Conduct

In order to foster a kind, inclusive, and harassment-free community, the Pinax Project
has a [code of conduct](http://pinaxproject.com/pinax/code_of_conduct/).
We ask you to treat everyone as a smart human programmer that shares an interest in Python, Django, and Pinax with you.


## Connect with Pinax

For updates and news regarding the Pinax Project, please follow us on Twitter [@pinaxproject](https://twitter.com/pinaxproject)
and check out our [Pinax Project blog](http://blog.pinaxproject.com).


## License

Copyright (c) 2012-2018 James Tauber and contributors under the [MIT license](https://opensource.org/licenses/MIT).