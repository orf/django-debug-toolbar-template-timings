from debug_toolbar.panels import DebugPanel
from django.conf import settings
from django.template.base import Template
from django.template.loader_tags import BlockNode, IncludeNode, ConstantIncludeNode
import threading
import functools
import time
import re
import collections

results = threading.local()
IGNORED_TEMPLATES = ["debug_toolbar/*"]

TEMPLATE_TIMINGS_SETTINGS = {
    'PRINT_TIMINGS': True,
}

TEMPLATE_TIMINGS_SETTINGS.update(getattr(settings, 'TEMPLATE_TIMINGS_SETTINGS', {}))


def _template_render_wrapper(func, key, should_add=lambda n: True, name=lambda s: s.name):

    @functools.wraps(func)
    def timing_hook(self, *args, **kwargs):
        # Set up our thread-local results cache
        if not hasattr(results, "timings"):
            results.timings = collections.defaultdict(dict)

        start_time = time.time()
        result = func(self, *args, **kwargs)
        time_taken = int(round((time.time() - start_time) * 1000))

        if should_add(name(self)):
            results.timings[key][name(self)] = time_taken
            if TEMPLATE_TIMINGS_SETTINGS['PRINT_TIMINGS']:
                print "%s %s took %s" % (key, name(self), time_taken)

        return result

    return timing_hook

Template.render = _template_render_wrapper(Template.render, "templates",
                                           lambda n: not any([re.match(pattern, n) for pattern in IGNORED_TEMPLATES]))
BlockNode.render = _template_render_wrapper(BlockNode.render, "blocks")
#IncludeNode.render = _template_render_wrapper(IncludeNode.render, "includes", name=lambda s: s.template_name)
#ConstantIncludeNode.render = _template_render_wrapper(ConstantIncludeNode.render, "includes",
#                                                      name=lambda s: s.template.name)


class TemplateTimings(DebugPanel):
    name = "TemplateTimingPanel"
    template = "debug_toolbar_template_timings.html"
    has_content = True

    def nav_title(self):
        return 'Template Timings'

    def title(self):
        return 'Template Timings'

    def url(self):
        return ''

    def process_response(self, request, response):
        if TEMPLATE_TIMINGS_SETTINGS['PRINT_TIMINGS']:
            print getattr(results, "timings", None)
        self.record_stats({"template_timings": getattr(results, "timings", None)})

