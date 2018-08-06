from setuptools import setup, find_packages


setup(
    name = "disney",
    version = "1.0",
    description = "A history of Shanghai Disney waiting time",
    long_description = "A history of Shanghai Disney waiting time",
    license = "Apache License",
    url = "http://s.gaott.info",
    author = "gtt116",
    author_email = "gtt116@gmail.com",
    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = [],

    scripts = [],
    entry_points = {
        'console_scripts': [
            'disney-fetch = disney.fetch:main',
            'disney-publish = disney.publish:main',
        ]
    }
)
