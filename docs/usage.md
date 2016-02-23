# Usage

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


## AdWords Conversion Tracking

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
