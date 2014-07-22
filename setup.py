#! /usr/bin/env python

import os
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy as np

incdirs = [os.getcwd(), np.get_include()]

ext_modules = [
    Extension("memleak.extra_types", ["memleak/extra_types.pyx"], 
              include_dirs=incdirs, language="c++"),
    Extension("memleak.stlcontainers", ["memleak/stlcontainers.pyx"], 
              include_dirs=incdirs, language="c++"),
    Extension("memleak.hollow", ['hollow.cpp', "memleak/hollow.pyx", ],
    	      include_dirs=incdirs, language="c++"),
    ]

setup(  
  name = 'memleak',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules,
  packages = ['memleak']
)
