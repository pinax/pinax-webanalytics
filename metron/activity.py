import json

from django.conf import settings


SESSION_KEY_NAME = getattr(settings, "METRON_ACTIVITY_SESSION_KEY_NAME", "_metron_activity")


def _key_name(kind):
    return SESSION_KEY_NAME + "-" + kind


def all(request, kind):
    actions = request.session.pop(_key_name(kind), None)
    if actions:
        for action in actions:
            action["args"] = list(action["args"])
            for i, arg in enumerate(action["args"]):
                if isinstance(action["args"][i], dict):
                    action["args"][i] = json.dumps(action["args"][i])
                else:
                    action["args"][i] = '"%s"' % action["args"][i]
    return actions


def add(request, kind, method, *args):
    """
    add(request, "mixpanel", "track", "purchase", {order: "1234", amount: "100"})
    add(request, "google", "push", ["_addTrans", "1234", "Gondor", "100"])
    """
    request.session.setdefault(_key_name(kind), []).append({
        "method": method,
        "args": args
    })
