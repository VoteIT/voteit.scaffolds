import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

requires = (
    'pyramid',
    'voteit.core',
    )

setup(name='voteit.scaffolds',
      version='0.0.1',
      description='VoteIT scaffolds',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='VoteIT development team and contributors',
      author_email='info@voteit.se',
      url='http://www.voteit.se',
      keywords='web pyramid pylons voteit',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires = requires,
      tests_require= requires,
      test_suite="voteit.scaffolds",
      entry_points = """\
      [pyramid.scaffold]
      voteit_buildout=voteit.scaffolds:BuildoutTemplate
      """,
      )
