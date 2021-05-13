from setuptools import find_packages, setup

VERSION = '0.0.1'
DESCRIPTION = 'Official tvdb api v4 package'
LONG_DESCRIPTION = 'Official python package for using the tvdb v4 api'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="tvdb-api-v4",
    version=VERSION,
    author="Weylin Wagnon",
    author_email="<wwagnon@whipmedia.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['python', 'first package'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Api users",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
