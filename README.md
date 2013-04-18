## Template-Timings

### About
Template-timings is a panel for [Django-debug-toolbar](https://github.com/django-debug-toolbar/django-debug-toolbar). Template-timings simply gives you a breakdown of the rendering process for your Django application, displaying the time each template (including templates rendered via {% extends %} and {% include %}) and block took to render.

### Why?
Django doesn't give you much insight as to why a template might take a long time to render. A block inside a template I was using added significant overhead in a non-obvious way, and I wished I had something like this to show exactly where the bottlekneck was.

### Install instructions
Install via pip (pip install django-debug-toolbar-template-timings). Then add __'template_timings_panel.panels.TemplateTimings.TemplateTimings'__ to your DEBUG_TOOLBAR_PANELS, and also add __'template_timings_panel'__ to your INSTALLED_APPS

### Preview
![](http://i.imgur.com/RyErSQn.png)
