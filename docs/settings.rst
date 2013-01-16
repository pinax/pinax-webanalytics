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

where the values you would supply for each service and ``SITE_ID`` node
is the identifier code for that service.

Note that, as of 1.1, the ``SITE_ID`` keys *must* be integers, not strings.
