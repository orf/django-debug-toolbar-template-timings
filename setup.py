from distutils.core import setup

setup(
    name='django-debug-toolbar-template-timings',
    version='0.2',
    packages=['template_timings_panel', 'template_timings_panel.panels'],
    package_data={'': ['templates/*']},
    url='',
    license='',
    author='Tom Forbes',
    author_email='tom@tomforb.es',
    description='A django-debug-toolbar panel that shows you template rendering times for Django',
    requires=['Django', 'debug_toolbar'],
)
