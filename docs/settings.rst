.. _settings:

Settings
========

.. _metron_settings:

METRON_SETTINGS
^^^^^^^^^^^^^^^

This is a data structure defining your analytics and metrics settings
indexed by `SITE_ID`. Example::

    ANALYTICS_SETTINGS = {
        "mixpanel": {
            "1": "", # production
            "2": "", # beta
        },
        "google": {
            "1": "", # production
            "2": "", # beta
        },
        "gauges": {
            "1": "",
        }
    }

Where the values you would supply for each service + `SITE_ID` node
is the identifier code for that service.