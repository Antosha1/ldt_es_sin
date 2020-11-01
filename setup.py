from setuptools import setup, find_packages


setup(
    name='es_sin',
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    author="Swimming in network",
    description="",

    install_requires=[
    ],

    entry_points={
        'console_scripts': [
            'start_es_sin = es_sin.main:main'
        ]
    })
