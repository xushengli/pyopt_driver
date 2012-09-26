#
# This file is autogenerated during plugin quickstart and overwritten during
# plugin makedist. DO NOT CHANGE IT if you plan to use plugin makedist to update 
# the distribution.
#

from setuptools import setup, find_packages

kwargs = {'author': 'Kenneth T. Moore',
 'author_email': 'kenneth.t.moore-1@nasa.gov',
 'classifiers': ['Intended Audience :: Science/Research',
                 'Topic :: Scientific/Engineering'],
 'description': 'OpenMDAO driver wrapper for the open-source optimization package pyOpt',
 'download_url': '',
 'entry_points': '[openmdao.component]\npyopt_driver.pyopt_driver.pyOptDriver=pyopt_driver.pyopt_driver:pyOptDriver\n\n[openmdao.driver]\npyopt_driver.pyopt_driver.pyOptDriver=pyopt_driver.pyopt_driver:pyOptDriver\n\n[openmdao.container]\npyopt_driver.pyopt_driver.pyOptDriver=pyopt_driver.pyopt_driver:pyOptDriver',
 'include_package_data': True,
 'install_requires': ['openmdao.main'],
 'keywords': ['openmdao'],
 'license': 'Apache License, Version 2.0',
 'maintainer': 'Kenneth T. Moore',
 'maintainer_email': 'kenneth.t.moore-1@nasa.gov',
 'name': 'pyopt_driver',
 'package_data': {'pyopt_driver': []},
 'package_dir': {'': 'src'},
 'packages': ['pyopt_driver'],
 'url': 'https://github.com/OpenMDAO-Plugins/pyopt-driver',
 'version': '0.7',
 'zip_safe': False}


setup(**kwargs)

