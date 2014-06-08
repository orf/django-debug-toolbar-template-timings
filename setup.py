from distutils.core import setup
import os

license = ""

if os.path.isfile("LICENSE"):
    with open('LICENSE') as f:
        license = f.read()


setup(
    zip_ok=False,
    name='django-debug-toolbar-template-timings',
    version='0.6.2',
    packages=['template_timings_panel', 'template_timings_panel.panels'],
    package_data={'': ['templates/*']},
    url='https://github.com/orf/django-debug-toolbar-template-timings',
    license=license,
    author='Tom Forbes',
    author_email='tom@tomforb.es',
    description='A django-debug-toolbar panel that shows you template rendering times for Django',
    install_requires=['Django', 'django-debug-toolbar>=1.0'],
    long_description=open('README.rst').read(),
    
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
          'Topic :: Software Development :: Debuggers']
)
