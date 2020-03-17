import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md')) as f:
    README = f.read()


setup(name='homebridge_huum_wrapper',
      version=0.1,
      description='HomeBridge HUUM.EU API wrapper',
      long_description=README,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pylons",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application"
      ],
      keywords="web services",
      author='Andres Kepler',
      author_email='andres@kepler.ee',
      url='https://github.com/kepsic/homebridge_huum_wrapper',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=['cornice', 'waitress', 'requests'],
      entry_points="""\
      [paste.app_factory]
      main=homebridge_huum_wrapper:main
      """,
      paster_plugins=['pyramid'])
