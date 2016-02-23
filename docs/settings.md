# Settings

## PINAX_WEBANALYTICS_ADWORDS_SETTINGS

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


## PINAX_WEBANALYTICS_SETTINGS

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
