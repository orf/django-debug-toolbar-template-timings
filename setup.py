from distutils.core import setup
import os

license = ""

if os.path.isfile("LICENSE"):
    with open('LICENSE') as f:
        license = f.read()

readme = ""

if os.path.isfile("README.rst"):
    with open("README.rst") as f:
        readme = f.read()


setup(
    name='django-debug-toolbar-template-timings',
    version='0.6.3',
    packages=['template_timings_panel', 'template_timings_panel.panels'],
    package_data={'': ['templates/*']},
    url='https://github.com/orf/django-debug-toolbar-template-timings',
    license=license,
    author='Tom Forbes',
    author_email='tom@tomforb.es',
    description='A django-debug-toolbar panel that shows you template rendering times for Django',
    install_requires=['Django', 'django-debug-toolbar>=1.0'],
    long_description=readme,
)
