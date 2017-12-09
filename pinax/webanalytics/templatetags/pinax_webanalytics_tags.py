from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

from .. import activity

register = template.Library()


@register.simple_tag(takes_context=True)
def analytics(context):
    content = ""
    for kind, codes in getattr(settings, "PINAX_WEBANALYTICS_SETTINGS", {}).items():
        site_id = getattr(context.get("request"), "pwa_site_id", settings.SITE_ID)
        code = codes.get(int(site_id))
        if code is not None and "user" in context and "request" in context:
            t = template.loader.get_template("pinax/webanalytics/_%s.html" % kind)
            content += t.render({
                "code": code,
                "user": context["user"],
                "actions": activity.all(context["request"], kind)
            })
    return mark_safe(content)


@register.simple_tag(takes_context=True)
def adwords_conversion(context, key):
    content = ""
    page_ids = getattr(settings, "PINAX_WEBANALYTICS_ADWORDS_SETTINGS", {}).get(key)
    if page_ids:
        t = template.loader.get_template("pinax/webanalytics/_adwords_conversion.html")
        content = t.render({
            "conversion_id": page_ids["conversion_id"],
            "conversion_format": page_ids["conversion_format"],
            "conversion_label": page_ids["conversion_label"]
        })
    return mark_safe(content)
