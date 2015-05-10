__author__ = 'JeffreyTang'

from setuptools import setup

setup(name='pyimage',
      version='0.1.0',
      description='A Python library for image processing',
      url='https://github.com/jyt109/pyimage',
      author='Jeffrey Tang',
      author_email='jeffrey.tang09@gmail.com',
      license='MIT',
      packages=['pyimage'],
      keywords='image processing pipeline',
      install_requires=['scikit-image', 'matplotlib', 'numpy']
      )

