#!/usr/bin/env python

from distutils.core import setup

setup(
    name="django-hash-field",
    version="0.01",
    description="Hash field for Django (stored in postgres as UUID)",
    author="Wouter van Atteveldt",
    author_email="wouter@vanatteveldt.com",
    packages=["django_hash_field"],
    keywords = ["django"],
    url = "https://github.com/amcat/django-hash-field",
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=[
        "django>=1.9",
    ],
)
