
================
Template-Timings
================

.. image:: https://img.shields.io/pypi/v/django-debug-toolbar-template-timings.svg
    :target: https://pypi.python.org/pypi/django-debug-toolbar-template-timings


Template-timings is a panel for Django Debug Toolbar that gives an in-dept breakdown of the time it takes to render your Django templates (including templates included via ``{% extends %}`` and ``{% include %}``).

Template-timings supports Django 1.8 and below, Django 1.9 and above do not work at the moment.

Install
=======

Install via pip (``pip install django-debug-toolbar-template-timings``) then add ``'template_timings_panel.panels.TemplateTimings.TemplateTimings'`` to your ``DEBUG_TOOLBAR_PANELS`` setting, and add ``'template_timings_panel'`` to your ``INSTALLED_APPS``::

    # http://django-debug-toolbar.readthedocs.org/en/latest/configuration.html#debug-toolbar-panels
    DEBUG_TOOLBAR_PANELS = [
        ...
        'template_timings_panel.panels.TemplateTimings.TemplateTimings',
    ]

    INSTALLED_APPS = [
        ...
        'template_timings_panel'
    ]


Screenshot
==========
.. image:: http://i.imgur.com/H2D48Uy.png


Frequently asked questions
==========================
**How much overhead does this add?**

In my experience this panel adds about 10% overhead. The panel uses the standard SQLPanel that ships with debug-toolbar to handle the SQL timings, so if you disable that the overhead will decrease and you can still see the render times.

**The SQL count is different from the SQLPanel?**

SQLPanel counts **all** queries that are executed, wherease this panel only counts queries that are executed while rendering a template.


Configuration
=============
Configuration is optional. There is currently only one setting you can configure (the values below are the default)::

    IGNORED_TEMPLATES = ["debug_toolbar/*"] # Ignore these templates from the output
