from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pcache",
    version="0.0.1",
    author="Pallab Pain",
    author_email="pallabkumarpain@gmail.com",
    description="A simple implementation of Persistent Caching",
    long_description=long_description,
    platforms="UNIX",
    url="https://github.com/pallabpain/pcache.git",
    package_dir="pcache",
    keywords=["cache", "persistent cache"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
)
