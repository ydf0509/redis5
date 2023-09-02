#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name="redis5",
    description="redis5 is forked from redis 5.0.0, so you can use redis5 and any version redis in one python env",
    long_description=open("README.md").read().strip(),
    long_description_content_type="text/markdown",
    keywords=["Redis", "key-value store", "database"],
    license="MIT",
    version="5.0.0",
    packages=find_packages(
        include=[
            "redis5",
            "redis5._parsers",
            "redis5.asyncio",
            "redis5.commands",
            "redis5.commands.bf",
            "redis5.commands.json",
            "redis5.commands.search",
            "redis5.commands.timeseries",
            "redis5.commands.graph",
            "redis5.parsers",
        ]
    ),
    package_data={"redis5": ["py.typed"]},
    include_package_data=True,
    url="https://github.com/ydf0509/redis5",
    project_urls={
        "Documentation": "https://redis.readthedocs.io/en/latest/",
        "Changes": "https://github.com/redis/redis-py/releases",
        "Code": "https://github.com/ydf0509/redis5",
        "Issue tracker": "https://github.com/redis/redis-py/issues",
    },
    author="Redis Inc.",
    author_email="oss@redis5.com",
    python_requires=">=3.7",
    install_requires=[
        'importlib-metadata >= 1.0; python_version < "3.8"',
        'typing-extensions; python_version<"3.8"',
        'async-timeout>=4.0.2; python_full_version<="3.11.2"',
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    extras_require={
        "hiredis": ["hiredis>=1.0.0"],
        "ocsp": ["cryptography>=36.0.1", "pyopenssl==20.0.1", "requests>=2.26.0"],
    },
)
