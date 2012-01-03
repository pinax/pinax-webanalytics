.. _templates:

Templates
=========

`metron` ships with templates for three services out of the box, gaug.es, Google
Analytics and Mixpanel. This can be overridden in your project for customizations
and likewise if there are other services you wish to use, just create a similar
template under the `metron` folder in your templates directory. The format is
`"_%s.html" % slug` where the slug is what index the `METRON_SETTINGS` dict with.


_guages.html
------------

This snippet is used for gaug.es


_google.html
------------

This snippet is used for Google Analytics


_mixpanel.html
--------------

This snippet is used for Mixpanel


_adwords_conversion.html
------------------------

This snippet is used by the `adwords_conversion` template tag
