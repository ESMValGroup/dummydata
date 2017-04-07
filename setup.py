# -*- coding: UTF-8 -*-

"""
This file is part of DUMMYDATA.
(c) 2016- Alexander Loew
For COPYING and LICENSE details, please refer to the LICENSE file
"""

from setuptools import setup
#~ from distutils.core import setup as setup_dist  # todo use only one setup


#~ from setuptools import setup, Extension
#~ from setuptools import find_packages  # Always prefer setuptools over distutils



# requires scipy:
install_requires = ["numpy>0.1", "netCDF4", "python-dateutil"]




#~ def get_current_version():
    #~ ppath = os.path.dirname(os.path.realpath(__file__))
    #~ return json.load(open(ppath + os.sep + 'geoval' + os.sep + 'version.json'))




setup(name='dummydata',

      version='0.1.3', #get_current_version(),

      description='dummydata - package for generation of random daa fields',

      author="Alexander Loew",
      author_email='alexander.loew@lmu.de',
      maintainer='Alexander Loew',
      maintainer_email='alexander.loew@lmu.de',

      license='APACHE 2.0',

      url='https://github.com/pygeo/dummydata',

      long_description='xxxx',

      # List run-time dependencies here. These will be installed by pip when your
      # project is installed. For an analysis of "install_requires" vs pip's
      # requirements files see:
      # https://packaging.python.org/en/latest/technical.html#install-requires-vs-requirements-files
      install_requires=install_requires,

      keywords=["data", "science", "climate", "meteorology",
                "model evaluation", "benchmarking", "metrics"],

      # To provide executable scripts, use entry points in preference to the
      # "scripts" keyword. Entry points provide cross-platform support and allow
      # pip to create the appropriate form of executable for the target
      # platform.

      #~ entry_points={
          #~ 'console_scripts': [
              #~ 'pycmbs_benchmarking = pycmbs_benchmarking:main'
          #~ ]},

      # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          # How mature is this project? Common values are
          # 3 - Alpha
          # 4 - Beta
          # 5 - Production/Stable
          # 'Development Status :: 4 - beta',
          # Indicate who your project is intended for
          #~ 'Intended Audience :: Science/Research',
          #~ 'Topic :: Scientific/Engineering :: Atmospheric Science',
          #~ 'Topic :: Scientific/Engineering :: GIS',
          #~ 'Topic :: Scientific/Engineering :: Visualization',

          # Pick your license as you wish (should match "license" above)
          # 'License :: OSI Approved :: Apache 2.0',

          # Specify the Python versions you support here. In particular, ensure
          # that you indicate whether you support Python 2, Python 3 or both.
          'Programming Language :: Python :: 2.7'
      ],

      #~ ext_modules=[ext_polygon_utils],
      #~ cmdclass={'build_ext': build_ext}

    #~ ext_modules=cythonize(
        #~ ["./geoval/polygon/polygon_utils.pyx"]),
    # this is needed to get proper information on numpy headers
    #~ include_dirs=[np.get_include()]

      )




########################################################################
# Some useful information on shipping packages
########################################################################

# PIP

# pypi documentation

# 1) on a new computer you need to create a .pypirc file like described in the
# pypi documentation
# 2) install twine using pip install twine
# 3) generate package using: python setup.py sdist
# 4) just upload using twine upload dist/*





