from setuptools import setup, find_packages

setup(
    name='test_framework',
    version='0.1.0',
    description='BDD-Testframework mit Page Object Pattern und Keyword-Layer',
    author='sija',
    packages=find_packages(),
    install_requires=[
        'behave',
        'selenium',
    ],
    include_package_data=True,
    python_requires='>=3.7',
)