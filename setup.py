# Package template taken from http://python-packaging.readthedocs.io
from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='lhcb_paper_2017_044',
      version='1.0',
      description='Supplementary material for LHCb-PAPER-2017-044.',
      long_description=readme(),
      url='http://github.com/lhcb/lhcb_paper_2017_044',
      author='LHCb Collaboration',
      author_email='lhcb-editorial-board-chair@cern.ch',
      license='MIT',
      packages=[
          'lhcb_paper_2017_044',
          'lhcb_paper_2017_044.tests'
      ],
      install_requires=[
          'hep_ml',
          'pandas'
      ],
      include_package_data=True,
      zip_safe=False)
