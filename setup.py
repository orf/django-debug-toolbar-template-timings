import os
from setuptools import setup

license = ""

if os.path.isfile("LICENSE"):
    with open('LICENSE') as f:
        license = f.read()

readme = ""

if os.path.isfile("README.rst"):
    with open("README.rst") as f:
        readme = f.read()


setup(
    zip_safe=False,
    name='django-debug-toolbar-template-timings',
    version='0.7',
    packages=['template_timings_panel', 'template_timings_panel.panels'],
    package_data={'': ['templates/*']},
    url='https://github.com/orf/django-debug-toolbar-template-timings',
    license=license,
    author='Tom Forbes',
    author_email='tom@tomforb.es',
    description='A django-debug-toolbar panel that shows you template rendering times for Django',
    install_requires=['Django', 'django-debug-toolbar>=1.0'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Debuggers'],

    long_description=readme,
)
