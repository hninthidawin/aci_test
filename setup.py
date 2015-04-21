import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()

requires = ['pyramid', 'WebError', 'pymongo']

setup(name='aci_test',
      version='0.0',
      description='aci_test',
      long_description=README,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author="Niall O'Higgins",
      author_email='nialljohiggins@gmail.com',
      url='https://github.com/niallo/pyramid_mongodb',
      keywords='web pyramid pylons mongodb',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=['requires', 'pyramid', 'pyramid_chameleon'],
      tests_require=requires,
      test_suite="aci_test",
      entry_points = """\
      [paste.app_factory]
      main = aci_test:main
      """,
      paster_plugins=['pyramid'],
      )

