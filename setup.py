#!/usr/bin/env python
"""The setup script."""

from setuptools import find_packages, setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['beautifulsoup4', 'fastapi', 'fire', 'requests', 'uvicorn']

test_requirements = [
    'pytest>=3',
    'mock',
]

setup(
    author="Javier Vegas-Regidor",
    author_email='javi_vegas@msn.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.10',
    ],
    description="FastApi exercise",
    entry_points={
        'console_scripts': [
            'getlinks = exercise.cli:run',
        ],
    },
    install_requires=requirements,
    extras_require={'test': test_requirements},
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='exercise',
    name='exercise',
    packages=find_packages(include=['exercise', 'exercise.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/jvegreg/exercise',
    version='0.1.0',
    zip_safe=False,
)
