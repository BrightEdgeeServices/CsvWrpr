'''Create a conftest.py

Define the fixture functions in this file to make them accessible across multiple test files.
'''
import datetime
from pathlib import Path
import pytest
import sys
from tempfile import mkdtemp
from beetools import get_os, msg_error, rm_tree
import configparserext
from github import Github, GithubException as gh_exc

_DESC = __doc__.split('\n')[0]
_PATH = Path(__file__)


_CLASSIFIERS = [
    'Development Status :: 1 - Planning',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Topic :: Software Development',
    'Topic :: System :: Systems Administration',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.0',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
]
_INDEX_RST_BADGE_CODECOV = '''.. image:: https://img.shields.io/codecov/c/gh/hendrikdutoit/csvwrpr
    :alt: CodeCov
    :target: https://app.codecov.io/gh/hendrikdutoit/csvwrpr

'''
_INDEX_RST_BADGE_GITHUB_CI = '''.. image:: https://img.shields.io/github/workflow/status/hendrikdutoit/csvwrpr/CI
    :alt: GitHub Actions - CI
    :target: https://github.com/hendrikdutoit/csvwrpr/actions/workflows/ci.yaml

'''
_INDEX_RST_BADGE_GITHUB_HITS = '''.. image:: https://img.shields.io/github/search/hendrikdutoit/csvwrpr/GitHub hit
    :alt: GitHub Searches

'''
_INDEX_RST_BADGE_GITHUB_LICENSE = '''.. image:: https://img.shields.io/github/license/hendrikdutoit/csvwrpr
    :alt: License

'''
_INDEX_RST_BADGE_GITHUB_ISSUES = '''.. image:: https://img.shields.io/github/issues-raw/hendrikdutoit/csvwrpr
    :alt: GitHub issues

'''
_INDEX_RST_BADGE_GITHUB_PRE_COMMIT = '''.. image:: https://img.shields.io/github/workflow/status/hendrikdutoit/csvwrpr/Pre-Commit
    :alt: GitHub Actions - Pre-Commit
    :target: https://github.com/hendrikdutoit/csvwrpr/actions/workflows/pre-commit.yaml

'''
_INDEX_RST_BADGE_GITHUB_RELEASE = '''.. image:: https://img.shields.io/github/v/release/hendrikdutoit/csvwrpr
    :alt: GitHub release (latest by date)

'''
_INDEX_RST_BADGE_PYPI_VERSION = '''.. image:: https://img.shields.io/testpypi/v/csvwrpr
    :alt: PyPi

'''
_INDEX_RST_BADGE_PYPI_DL = '''.. image:: https://img.shields.io/pypi/dm/csvwrpr
    :alt: PyPI - Downloads

'''
_INDEX_RST_BADGE_PYPI_STATUS = '''.. image:: https://img.shields.io/pypi/status/csvwrpr
    :alt: PyPI - Status

'''
_INDEX_RST_BADGE_PYPI_WHEEL = '''.. image:: https://img.shields.io/pypi/wheel/csvwrpr
    :alt: PyPI - Wheel

'''
_INDEX_RST_BADGE_PYVERSIONS = '''.. image:: https://img.shields.io/pypi/pyversions/csvwrpr
    :alt: PyPI - Python Version

'''
_INDEX_RST_CONTENTS = '''.. ======================================================
.. This file is auto generated by PackageIt. Any changes
.. to it will be over written
.. ======================================================

================================
csvwrpr
================================

.. image:: https://img.shields.io/pypi/status/csvwrpr
    :alt: PyPI - Status

.. image:: https://img.shields.io/pypi/wheel/csvwrpr
    :alt: PyPI - Wheel

.. image:: https://img.shields.io/pypi/pyversions/csvwrpr
    :alt: PyPI - Python Version

.. image:: https://img.shields.io/github/v/release/hendrikdutoit/csvwrpr
    :alt: GitHub release (latest by date)

.. image:: https://img.shields.io/github/license/hendrikdutoit/csvwrpr
    :alt: License

.. image:: https://img.shields.io/github/issues-raw/hendrikdutoit/csvwrpr
    :alt: GitHub issues

.. image:: https://img.shields.io/pypi/dm/csvwrpr
    :alt: PyPI - Downloads

.. image:: https://img.shields.io/github/search/hendrikdutoit/csvwrpr/GitHub hit
    :alt: GitHub Searches

.. image:: https://img.shields.io/codecov/c/gh/hendrikdutoit/csvwrpr
    :alt: CodeCov
    :target: https://app.codecov.io/gh/hendrikdutoit/csvwrpr

.. image:: https://img.shields.io/github/workflow/status/hendrikdutoit/csvwrpr/Pre-Commit
    :alt: GitHub Actions - Pre-Commit
    :target: https://github.com/hendrikdutoit/csvwrpr/actions/workflows/pre-commit.yaml

.. image:: https://img.shields.io/github/workflow/status/hendrikdutoit/csvwrpr/CI
    :alt: GitHub Actions - CI
    :target: https://github.com/hendrikdutoit/csvwrpr/actions/workflows/ci.yaml

.. image:: https://img.shields.io/testpypi/v/csvwrpr
    :alt: PyPi

Project Header Description (default ini)

    Project long description goes in here (default ini)

------------
Installation
------------

.. code-block:: bash

    $ pip install .

-----
Usage
-----

.. code-block:: bash

    Insert text in Usage.rst

-------
Support
-------

.. code-block:: bash

    Insert text in Support.rst

.. toctree::
    :maxdepth: 2
    :caption: Contents
    :numbered:

    conventions
    api
    donotexist

'''
_PROJECT_CLASSIFIERS = [
    'Development Status :: 1 - Planning',
    'Intended Audience :: Developers',
    'Topic :: Software Development',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.0',
    'Programming Language :: Python :: 3.10',
]


_PROJECT_NAME = "csvwrpr"
_RELEASE_YAML_PROD = '''name: Build distribution

on: [push, pull_request]

jobs:
  ReleaseToPyPi:
    runs-on: "ubuntu-latest"

    steps:
      - name: Checkout source
        uses: actions/checkout@v2

      - name: Set up Python 3.9
        uses: actions/setup-python@v1
        with:
          python-version: 3.9

      - name: Install build dependencies
        run: python -m pip install build wheel

      - name: Build distributions
        shell: bash -l csvwrpr
        run: python setup.py sdist bdist_wheel

      - name: Publish package to PyPI
        uses: pypa/gh-action-pypi-publish@master
        with:
          user: __token__
          password: ${{ secrets.PYPI_API_TOKEN }}
          repository_url: https://upload.pypi.org/legacy/
          verbose: true
'''
_RELEASE_YAML_TEST = '''name: Build distribution

on: [push, pull_request]

jobs:
  ReleaseToPyPi:
    runs-on: "ubuntu-latest"

    steps:
      - name: Checkout source
        uses: actions/checkout@v2

      - name: Set up Python 3.9
        uses: actions/setup-python@v1
        with:
          python-version: 3.9

      - name: Install build dependencies
        run: python -m pip install build wheel

      - name: Build distributions
        shell: bash -l csvwrpr
        run: python setup.py sdist bdist_wheel

      - name: Publish package to PyPI
        uses: pypa/gh-action-pypi-publish@master
        with:
          user: __token__
          password: ${{ secrets.TEST_PYPI_API_TOKEN }}
          repository_url: https://test.pypi.org/legacy/
          verbose: true
'''


class WorkingDir:
    def __init__(self):
        self.dir = Path(mkdtemp(prefix='packageit_'))


class EnvSetUp:
    def __init__(self, p_make_project_ini=False):
        self.project_name = self.make_project_name()
        self.dir = WorkingDir().dir
        self.classifiers = _CLASSIFIERS
        self.external_arc_dir = self.dir / 'external_archive'
        self.external_arc_dir.mkdir(parents=True)
        self.index_rst_badge_codecov = _INDEX_RST_BADGE_CODECOV.format(
            self.project_name
        )
        self.index_rst_badge_github_ci = _INDEX_RST_BADGE_GITHUB_CI.format(
            self.project_name
        )
        self.index_rst_badge_github_license = _INDEX_RST_BADGE_GITHUB_LICENSE.format(
            self.project_name
        )
        self.index_rst_badge_github_hits = _INDEX_RST_BADGE_GITHUB_HITS.format(
            self.project_name
        )
        self.index_rst_badge_github_issues = _INDEX_RST_BADGE_GITHUB_ISSUES.format(
            self.project_name
        )
        self.index_rst_badge_github_pre_commit = (
            _INDEX_RST_BADGE_GITHUB_PRE_COMMIT.format(self.project_name)
        )
        self.index_rst_badge_github_release = _INDEX_RST_BADGE_GITHUB_RELEASE.format(
            self.project_name
        )
        self.index_rst_badge_pypi_version = _INDEX_RST_BADGE_PYPI_VERSION.format(
            self.project_name
        )
        self.index_rst_badge_pypi_dl = _INDEX_RST_BADGE_PYPI_DL.format(
            self.project_name
        )
        self.index_rst_badge_pypi_status = _INDEX_RST_BADGE_PYPI_STATUS.format(
            self.project_name
        )
        self.index_rst_badge_pypi_wheel = _INDEX_RST_BADGE_PYPI_WHEEL.format(
            self.project_name
        )
        self.index_rst_badge_pyversions = _INDEX_RST_BADGE_PYVERSIONS.format(
            self.project_name
        )
        self.index_rst_contents = _INDEX_RST_CONTENTS.format(self.project_name)
        self.project_classifiers = _PROJECT_CLASSIFIERS
        self.packageit_ini_pth = self.make_packageit_ini()
        self.project_ini_pth = None
        self.release_yaml_prod = _RELEASE_YAML_PROD
        self.release_yaml_test = _RELEASE_YAML_TEST
        self.token_dir = Path('d:\\', 'dropbox', 'lib', 'SSHKeys')
        self.token_gh_pth = self.token_dir / 'github_token.txt'
        self.token_pypi_pth = self.token_dir / 'PYPI_API_TOKEN.txt'
        self.token_testpypi_pth = self.token_dir / 'TEST_PYPI_API_TOKEN.txt'
        self.token_rtd_pth = self.token_dir / 'readthedocs_token.txt'

        if p_make_project_ini:
            self.project_ini_pth = self.make_project_ini()

    def create_mock_files(self):
        project_root_dir = self.dir / self.project_name
        src_dir = project_root_dir / 'src' / self.project_name.lower()
        (src_dir / '{}.py'.format(self.project_name.lower())).write_text(
            'Test file\nThis file is included'
        )
        (src_dir / '{}.pyc'.format(self.project_name.lower())).write_text(
            'Test file\nThis file is excluded'
        )
        (src_dir / '{}.ini'.format(self.project_name.lower())).write_text('[Folders]\n')
        pass

    def del_github_repo(self):
        token = self.token_gh_pth.read_text().strip()
        g_hub = Github(login_or_token=token)
        gh_user = g_hub.get_user()
        try:
            repo = gh_user.get_repo(self.project_name)
            repo.delete()
        except gh_exc as err:
            if err.status != 404:  # Repo does not exist
                print(
                    msg_error(
                        '{} - {}\nSystem terminated.'.format(
                            err.status, err.data['message']
                        )
                    )
                )
                sys.exit()
        pass

    def make_packageit_ini(self):
        '''Make INI file for testing'''
        packageit_ini_pth = self.dir / 'pimt.ini'
        ini = configparserext.ConfigParserExt(inline_comment_prefixes="#")
        ini['Classifiers'] = {
            'DevStatus': 'Development Status :: 1 - Planning',
            'IntendedAudience002': 'Intended Audience :: Developers',
            'IntendedAudience013': 'Intended Audience :: System Administrators',
            'Topic013': 'Topic :: Software Development',
            'Topic027': 'Topic :: System :: Systems Administration',
            'License': 'License :: OSI Approved :: MIT License',
            'ProgrammingLanguage001': 'Programming Language :: Python :: 3.0',
            'ProgrammingLanguage010': 'Programming Language :: Python :: 3.9',
            'ProgrammingLanguage011': 'Programming Language :: Python :: 3.10',
        }
        ini['Coverage'] = {'Omit010': 'setup.py'}
        ini['Detail'] = {
            'Author': 'Ann Other',
            'AuthorEmail': 'ann.other@testmodule.com',
            'HeaderDescription': 'Project Header Description (default ini)',
            'LongDescription': 'Project long description goes in here (default ini)',
            '{}ProjectAnchorDir'.format(get_os()): self.dir,
            '{}ProjectIniDir'.format(get_os()): Path(self.dir, 'ini'),
            'PythonRequires': '>=3.6',
            'Url': 'www.{}.com'.format(self.project_name.lower()),
            'Type': 'Module',
        }

        ini['flake8'] = {
            'exclude': '__init__.py, VersionArchive /, Archive /',
            'max-line-length': '120',
        }
        ini['General'] = {'Verbose': 'Yes'}
        ini['Git'] = {
            'Enable': 'Yes',
            #     'Include' : '*.py;*.ini;*.bat;*.sh',
            #     'Ignore'  : '/VersionArchive;.workspace/;__pycache__/;*.komodoproject;*.log'
        }
        ini['GitHub'] = {
            'BugTemplate': 'templ_github_bug.md',
            'ConfigTemplate': 'templ_github_config.yaml',
            'Enable': 'Yes',
            'FeatureTemplate': 'templ_github_feature.md',
            'TokenFileName': 'github_token.txt',
            'UserName': 'hendrikdutoit',
            'Url': 'https: // github.com',
        }
        ini['Import'] = {
            'ReWrite': 'Yes',
            'Prod01': 'pypi;termcolor',
            'Test01': 'pypi;pip',
            'Test02': 'pypi;wheel',
            'Test03': 'pypi;pre-commit',
            'Test04': 'pypi;pytest',
            'Test05': 'pypi;beetools',
            'Test06': 'pypi;pytest-cov',
            'Test07': 'pypi;sphinx',
            'Test08': 'pypi;sphinx-autobuild',
            'Test09': 'pypi;black',
            'Test10': 'pypi;build',
            'Test11': 'pypi;configparserext',
            'Test12': 'pypi;pygithub',
        }
        ini['Install Apps'] = {'App01': 'pre-commit install'}
        ini['LogLevels'] = {'Default': 0, 'Console': 0, 'File': 0}
        ini['PyPi'] = {
            'Publishing': 'GitHub',  # No | GitHub| Twine
            'Repository': 'testpypi',
            'TokenFileNamePyPi': 'PYPI_API_TOKEN.txt',
            'TokenFileNameTestPyPi': 'TEST_PYPI_API_TOKEN.txt',
        }
        ini['ReadTheDocs'] = {
            'Enable': 'Yes',
            'ConfigTemplate': 'readthedocs_def_.readthedocs_template.yaml',
            'NewProjectTemplate': 'readthedocs_def_newproject_template.json',
            'TokenFileName': 'readthedocs_token.txt',
        }
        ini['Sphinx'] = {
            'Enable': "Yes",
            'ConfPyInstr001': "extensions = ['sphinx.ext.autodoc']",
            'ConfPyInstr010': "templates_path = ['_templates']",
            'ConfPyInstr020': "language = 'en'",
            'ConfPyInstr030': "exclude_patterns = []",
            'ConfPyInstr040': "html_theme = 'agogo'",
            'ConfPyInstr050': "html_static_path = ['_static']",
            'AddSection001': "Installation",
            'AddSection010': "Usage",
            'AddSection020': "Support",
            'AddContent001': "conventions",
            'AddContent010': "api",
            'AddContent020': "donotexist",
        }
        ini['tool:pytest'] = {
            'addopts_cmd': '--doctest-modules '
            '--cov=tests --cov=packageit '
            '--ignore-glob=*/VersionArchive '
            '--ignore-glob=*/Archive '
            '--ignore-glob=*/Templates '
            '--cov-report=html',
            'addopts_ide': '--ignore-glob=*/VersionArchive '
            '--ignore-glob=*/Archive '
            '--cov-report=html',
        }
        ini['VEnv'] = {
            'Enable': 'Yes',
            'Upgrade': 'Yes',
            'ReinstallVEnv': 'No',
            '{}VEnvBaseFolder'.format(get_os()): self.dir,
            '{}VEnvAnchorDir'.format(get_os()): self.dir / 'venv',
        }
        with open(packageit_ini_pth, 'w') as ini_file:
            ini.write(ini_file)
        return packageit_ini_pth

    def make_project_ini(self):
        '''Make a project specific ini file'''
        project_ini_pth = Path(
            self.packageit_ini_pth.parents[0],
            self.project_name,
            '.packageit',
            'packageit.ini',
        )
        if not project_ini_pth.parents[0].exists():
            project_ini_pth.parents[0].mkdir(parents=True)
        ini = configparserext.ConfigParserExt(inline_comment_prefixes="#")
        ini['Classifiers'] = {
            'DevStatus': 'Development Status :: 1 - Planning',
            'IntendedAudience002': 'Intended Audience :: Developers',
            'IntendedAudience003': 'Intended Audience :: System Administrators',
            'Topic013': 'Topic :: Software Development',
            'License': 'License :: OSI Approved :: MIT License',
            'ProgrammingLanguage001': 'Programming Language :: Python :: 3.0',
            'ProgrammingLanguage011': 'Programming Language :: Python :: 3.10',
        }
        ini['Coverage'] = {}
        ini['Detail'] = {
            'Author': 'Hendrik du Toit',
            'AuthorEmail': 'hendrik@brightedge.co.za',
            'HeaderDescription': 'Project Header Description (project ini)',
            'Import01': 'import sys',
            'LongDescription': 'Project long description goes in here (project ini)',
            'Url': 'www.brightedge.co.za',
        }
        ini['flake8'] = {
            'exclude': '__init__.py, VersionArchive /, Archive /',
            'max-line-length': '120',
        }
        ini['General'] = {'Verbose': 'Yes'}
        ini['Git'] = {}
        ini['GitHub'] = {'UserName': 'hendrikdutoit', 'Url': 'https: // github.com'}
        ini['Import'] = {}
        ini['Install Apps'] = {}
        ini['LogLevels'] = {}
        ini['PyPi'] = {}
        ini['Sphinx'] = {}
        ini['tool:pytest'] = {
            'addopts_cmd': '--doctest-modules '
            '--cov = tests '
            '--cov=packageit '
            '--ignore-glob=*/VersionArchive '
            '--ignore-glob=*/Archive '
            '--ignore-glob=*/Templates '
            '--cov-report=html',
            'addopts_ide': '--ignore-glob=*/VersionArchive '
            '--ignore-glob=*/Archive '
            '--cov-report=html',
        }
        ini['VEnv'] = {}
        with open(project_ini_pth, 'w') as project_ini_file:
            ini.write(project_ini_file)
        return project_ini_pth

    def make_project_name(self):
        return '{}_{}'.format(
            _PROJECT_NAME, datetime.datetime.now().strftime('%y%m%d%H%M%S%f')
        )


@pytest.fixture
def env_setup_self_destruct():
    '''Set up the environment base structure'''
    setup_env = EnvSetUp()
    yield setup_env
    rm_tree(setup_env.dir, p_crash=False)


@pytest.fixture
def env_setup_with_project_ini_self_destruct():
    '''Set up the environment base structure'''
    setup_env = EnvSetUp(p_make_project_ini=True)
    yield setup_env
    rm_tree(setup_env.dir, p_crash=False)


@pytest.fixture
def working_dir_self_destruct():
    '''Set up the environment base structure'''
    working_dir = WorkingDir()
    yield working_dir
    rm_tree(working_dir.dir, p_crash=False)
