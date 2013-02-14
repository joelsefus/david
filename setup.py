import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'SQLAlchemy',
    'transaction',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'zope.sqlalchemy',
    'Mako',
    'docutils',
    'feedparser',
    'mechanize',
    'beautifulsoup4',
    'pyramid-beaker',
    'pyramid-rpc',
    'pyramid-layout',
    'WebError',
    'FormEncode',
    'WTForms',
    'trumpet>=0.1.1dev', # pull from github
    'hubby>=0.0dev',   # pull from github
    'waitress',
    ]

setup(name='david',
      version='0.0',
      description='david',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='david',
      install_requires=requires,
      dependency_links=[
        'https://github.com/umeboshi2/trumpet/archive/master.tar.gz#egg=trumpet-0.1.1dev',
        'https://github.com/umeboshi2/hubby/archive/master.tar.gz#egg=hubby-0.0dev',
        ],
      entry_points="""\
      [paste.app_factory]
      main = david:main
      [console_scripts]
      initialize_david_db = david.scripts.initializedb:main
      [fanstatic.libraries]
      trumpet = trumpet.resources:library
      """,
      )
