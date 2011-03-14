#!/usr/bin/env python

import sys
assert sys.version >= '2.5', "Requires Python v2.5 or above"
from distutils.core import setup, Extension

setup(
    name="songtaggr",
    version="0.1",
    author="Shivanand Velmurugan",
    author_email="shiv@shiv.me",
    url="http://github.com/shiva/songtaggr/",
    description="mp3 tag information retrieval & update.",
    long_description="Retrieves idv1/2 information such as artist, title, album duration, etc., and provides a simple interface to update tags for a list of files ",
    license="FreeBSD",
    packages=['songtaggr'],
    package_dir={'songtaggr': 'src/songtaggr'}
)
