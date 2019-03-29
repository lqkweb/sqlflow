#!/usr/bin/env python

from distutils.core import setup

setup(name='pysqlflow',
      version='0.0.1',
      description='SQL Machine learning platform',
      long_description=open('README.md').read(),
      long_description_content_type="text/markdown",
      author='lqkweb',
      author_email='798244092@qq.com',
      url='https://github.com/lqkweb/sqlflow/tree/master',
      packages=['sqlflow'],
      license='LICENSE.txt',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Operating System :: OS Independent',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python',
          'Programming Language :: Python :: Implementation',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Libraries'
      ],
      )

# python setup.py sdist && python setup.py sdist upload && pip install --upgrade masql
# https://www.jianshu.com/u/3fe4aab60ac4
# http://www.leiqiankun.com/