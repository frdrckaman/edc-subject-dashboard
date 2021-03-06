# -*- coding: utf-8 -*-
import os
from setuptools import setup
from setuptools import find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

with open(os.path.join(os.path.dirname(__file__), 'VERSION')) as f:
    VERSION = f.read()

tests_require = ['edc_test_utils']
with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    for line in f:
        tests_require.append(line.strip())

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='edc-subject-dashboard',
    version=VERSION,
    author=u'Erik van Widenfelt',
    author_email='ew2789@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='http://github/clinicedc/edc-subject-dashboard',
    license='GPL license, see LICENSE',
    description='Subject dashboard classes for clinicedc/edc projects',
    long_description=README,
    zip_safe=False,
    keywords='edc subject dashboard',
    install_requires=[
        'edc-locator',
        'edc-dashboard',
        'edc-data-manager',
        'edc-registration',
        'edc-action-item',
        'edc-appointment',
        'edc-consent',
        'edc-lab',
        'edc-metadata',
        'edc-model-wrapper',
        'edc-notification',
        'edc-prn',
        'edc-visit-schedule',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    python_requires=">=3.7",
    tests_require=tests_require,
    test_suite='runtests.main',
)
