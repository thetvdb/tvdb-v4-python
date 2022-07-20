from setuptools import find_packages, setup

VERSION = '1.0.11'
DESCRIPTION = 'Official tvdb api v4 package'
LONG_DESCRIPTION = 'Official python package for using the tvdb v4 api'

# Setting up
setup(
    name="tvdb_v4_official",
    version=VERSION,
    author="Weylin Wagnon",
    author_email="<support@thetvdb.com>",
    url='https://github.com/thetvdb/tvdb-v4-python',
    description="tvdb-api-v4 utility package",
    long_description="official python client for the tvdb api v4",
    packages=find_packages(),
    install_requires=[],
    py_modules=['tvdb_v4_official'],
    keywords=['python', 'tvdb'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    package_dir={'tvdb_v4_official': 'tvdb_v4_official'}
)
