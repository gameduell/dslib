from setuptools import setup, find_packages

setup(
    name = "dslib",
    version = "0.1",
    packages = find_packages(),
    scripts = [],
    install_requires = [
            'pandas',
            'pysupplies'
            ],
    package_data = {
        '': ['*.txt', '*.rst'],
    },

    # metadata for upload to PyPI
    author = "wabu",
    author_email = "wabu@fooserv.net",
    description = "python data science libs developed at GameDuell",
    license = "MIT",
)
