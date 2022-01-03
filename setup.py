from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='calcul',
  version='0.0.2',
  description='Calculator that takes a string as input',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',
  author='AgungAndre',
  author_email='agungandre687@gmail.com',
  license='MIT',
  classifiers=classifiers,
  keywords='calculator',
  packages=find_packages(),
  install_requires=['']
)
