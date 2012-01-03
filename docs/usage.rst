.. _usage:

Usage
=====

Integrating `metron` quite simple::

    {% load  metron_tags %}

and then toward the bottom of the body where you put your scripts::

    {% analytics %}


If you want to add certain specific activities you can use the activity
API in `metron` like so::

    from metron import activity
    
    activity.add(request, "mixpanel", "track", "Node Viewed", {
        "node": self.get_object().title,
        "user": request.user.username
    })

You would typically want to call this within a view where you had some
activity you wanted to track that was more transactional than could be
determined by simply a certain page view.

The parameters for this are the request, the kind, then the method that
is used on the kind's javascript API, followed by a list of args that
will be passed to that javascript API.


AdWords Converstion Tracking
----------------------------

::
    {% load metron_tags %}
    
    {% adwords_conversion "waitinglist" %}

