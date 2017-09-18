from setuptools import setup, find_packages


def readme():
    with open("README.md", 'r') as f:
        return f.read()


setup(
    name="nothashes",
    description="Wrapper classes for zlib.crc32 and zlib.alder32 " +
    "that make them behave like hashlib classes.",
    version="1.0.2",
    long_description=readme(),
    author="Brian Balsamo",
    author_email="brian@brianbalsamo.com",
    packages=find_packages(
        exclude=[
        ]
    ),
    include_package_data=True,
    url='https://github.com/bnbalsamo/nothashes',
    install_requires=[
    ],
    tests_require=[
        'pytest'
    ],
    test_suite='tests'
)
