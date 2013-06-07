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
        time_taken = (time.time() - start_time) * 1000.0

        name_self = name(self)
        if should_add(name_self):
            if name_self not in results.timings[key]:
                results.timings[key][name_self] = {
                    'count': 0,
                    'min': None,
                    'max': None,
                    'total': 0,
                    'avg': 0,
                }
            results_part = results.timings[key][name_self]
            if results_part['min'] is None or time_taken < results_part['min']:
                results_part['min'] = time_taken
            if results_part['max'] is None or time_taken > results_part['max']:
                results_part['max'] = time_taken
            results_part['count'] += 1
            results_part['total'] += time_taken
            results_part['avg'] = results_part['total'] / results_part['count']
            if TEMPLATE_TIMINGS_SETTINGS['PRINT_TIMINGS']:
                print "%s %s took %.1f" % (key, name_self, time_taken)

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

    def _get_timings(self):
        return getattr(results, "timings", None)

    def nav_title(self):
        return 'Template Timings'

    def title(self):
        return 'Template Timings'

    def url(self):
        return ''

    def process_response(self, request, response):
        timings = self._get_timings()
        if TEMPLATE_TIMINGS_SETTINGS['PRINT_TIMINGS']:
            print timings
        # Setting default_factory to None allows us to access
        # template_timings.iteritems in the template.
        timings.default_factory = None
        self.record_stats({"template_timings": timings})
