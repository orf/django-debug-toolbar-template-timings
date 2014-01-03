## Template-Timings

### About
[Django templates are slow](http://tomforb.es/just-how-slow-are-django-templates?pid=0). Template-timings is a panel for [Django-debug-toolbar](https://github.com/django-debug-toolbar/django-debug-toolbar) shows you exactly how slow each of your templates and blocks are in your Django application, displaying the time each template (including templates rendered via {% extends %} and {% include %}) and block took to render. It also includes the number of SQL statements each template or block executed as well as the min/max time.

### Why?
Django doesn't give you much insight as to why a template might take a long time to render. A block inside a template I was using added significant overhead in a non-obvious way, and I wished I had something like this to show exactly where the bottlekneck was.

### FAQ
#### How much overhead does this add?
In my experience this panel adds about 10% overhead. The panel uses the standard SQLPanel that ships with debug-toolbar to handle the SQL timings, so if you disable that the overhead will decrease and you can still see the render times.

#### The SQL count is different from the SQLPanel?
SQLPanel counts **all** queries that are executed, wherease this panel only counts queries that are executed while rendering a template.

### Install instructions
Install via pip (pip install django-debug-toolbar-template-timings). Then add __'template_timings_panel.panels.TemplateTimings.TemplateTimings'__ to your DEBUG_TOOLBAR_PANELS, and also add __'template_timings_panel'__ to your INSTALLED_APPS.

### Configuration
Configuration is optional. There is currently only one setting you can configure (the values below are the default):

    IGNORED_TEMPLATES = ["debug_toolbar/*"] # Ignore these templates from the output


### Preview
![](http://i.imgur.com/5krqT6P.png)


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/orf/django-debug-toolbar-template-timings/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

