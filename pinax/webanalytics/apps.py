from django.apps import AppConfig as BaseAppConfig
from django.utils.translation import ugettext_lazy as _


class AppConfig(BaseAppConfig):

    name = "pinax.webanalytics"
    label = "pinax-webanalytics"
    verbose_name = _("Pinax Web Analytics")
