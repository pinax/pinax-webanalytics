.. _settings:

Settings
========

.. _metron_settings:

METRON_ADWORDS_SETTINGS
^^^^^^^^^^^^^^^^^^^^^^^

This sets the conversion identifiers for AdWords for the conversions
you want to track indexed by page specific keys::

    METRON_ADWORDS_SETTINGS = {
        "waitinglist": {
            "conversion_id": "",
            "conversion_label": "",
            "conversion_format": ""
        }
    }


METRON_SETTINGS
^^^^^^^^^^^^^^^

This is a data structure defining your analytics and metrics settings
indexed by `SITE_ID`. Example::

    METRON_SETTINGS = {
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
