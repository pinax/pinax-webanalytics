from django import template
from django.conf import settings

from metron import activity


register = template.Library()


@register.simple_tag(takes_context=True)
def analytics(context):
    content = ""
    for kind, codes in getattr(settings, "METRON_SETTINGS", {}).items():
        site_id = getattr(context.get("request"), "metron_site_id", settings.SITE_ID)
        code = codes.get(int(site_id))
        if code is not None and "user" in context and "request" in context:
            t = template.loader.get_template("metron/_%s.html" % kind)
            content += t.render(template.Context({
                "code": code,
                "user": context["user"],
                "actions": activity.all(context["request"], kind)
            }))
    return content


@register.simple_tag(takes_context=True)
def adwords_conversion(context, key):
    content = ""
    page_ids = getattr(settings, "METRON_ADWORDS_SETTINGS", {}).get(key)
    if page_ids:
        t = template.loader.get_template("metron/_adwords_conversion.html")
        content = t.render(template.Context({
            "conversion_id": page_ids["conversion_id"],
            "conversion_format": page_ids["conversion_format"],
            "conversion_label": page_ids["conversion_label"]
        }))
    return content
