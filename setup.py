#!/usr/bin/env python
        
from setuptools import setup, find_packages

setup(name='conpy',
      version='0.1.0',
      description='Convenient configuration handling',
      author='Max F. Hantke',
      author_email='maxhantke@gmail.com',
      url='https://github.com/mhantke/conpy',
      # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Physics',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: BSD License',

        
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        #'Programming Language :: Python :: 3',
        #'Programming Language :: Python :: 3.2',
        #'Programming Language :: Python :: 3.3',
        #'Programming Language :: Python :: 3.4',
      ],
      keywords='configuration file dictionary data types',
      #install_requires=['numpy', 'multiprocessing', 'h5py', 'mpi4py>=2.0.0'],
      packages = ['conpy'],
)   
    
