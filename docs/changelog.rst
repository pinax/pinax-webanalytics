.. _changelog:

ChangeLog
=========

1.3
---

- site ID keys in METRON_SETTINGS can reference the value stored in
  ``request.metron_site_id`` (useful for multi-tenancy setups)

1.2
---

- Upgraded mixpanel


1.1
---

- ``SITE_ID`` is now always treated as an int on lookup so the keys in
  ``METRON_SETTINGS`` must be ints
- analytics template tag now bails out silently if ``user`` or ``request`` are
  missing from context

1.0
---

- same as 0.2

0.2
---

- added activity tracking
- added adwords conversion tracking (per page template tag)

0.1
---

- initial release
