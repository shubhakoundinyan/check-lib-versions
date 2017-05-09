#!	/usr/bin/python
#	encoding: utf-8

#	The following script will help to check the libraries and the corresponding versions

#	This is important information to verify and validate before we begin Machine Learning programming

#	The ideology and code credit : Dr. Jason Brownlee, vivid Machine Learning practioner

# Python version
import sys
print("\nPython: v{}".format(sys.version))

# numpy = The fundamental package for scientific computing
import numpy
print("\nNumPy: v{}".format(numpy.__version__))

# scipy = The scientific and technical computing module
import scipy
print('SciPy: v{}'.format(scipy.__version__))

# pandas = Python package providing fast, flexible, and expressive data structures designed to make working with “relational” or “labeled” data both easy and intuitive
import pandas
print('Pandas: v{}'.format(pandas.__version__))

# matplotlib = The plotting library for the Python programming language and its numerical mathematics extension NumPy
import matplotlib
print('MatPlotLib: v{}'.format(matplotlib.__version__))

# scikit-learn = The software machine learning library. It includes various algorithms, and is designated to interoperate seamlessly with NumPy and SciPy
import sklearn
print('SciKit-Learn: v{}'.format(sklearn.__version__))