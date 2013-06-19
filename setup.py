from distutils.core import setup
import os

license = ""

if os.path.isfile("LICENSE"):
    with open('LICENSE') as f:
        license = f.read()


setup(
    name='django-debug-toolbar-template-timings',
    version='0.4.1',
    packages=['template_timings_panel', 'template_timings_panel.panels'],
    package_data={'': ['templates/*']},
    url='https://github.com/orf/django-debug-toolbar-template-timings',
    license=license,
    author='Tom Forbes',
    author_email='tom@tomforb.es',
    description='A django-debug-toolbar panel that shows you template rendering times for Django',
    requires=['Django', 'debug_toolbar'],
)
