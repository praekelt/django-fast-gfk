import multiprocessing
from setuptools import setup, find_packages


setup(
    name="django-fast-gfk",
    version="0.1",
    description="Do Django generic foreign key lookups in one query",
    long_description = open("README.rst", "r").read() + open("AUTHORS.rst", "r").read() + open("CHANGELOG.rst", "r").read(),
    author="Praekelt Consulting",
    author_email="dev@praekelt.com",
    license="BSD",
    url="http://github.com/praekelt/django-fast-gfk",
    packages = find_packages(),
    install_requires = [
        "django",
    ],
    include_package_data=True,
    tests_require=[
        "tox",
    ],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
