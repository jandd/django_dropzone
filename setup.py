from setuptools import setup, find_packages

setup(
    name='django_dropzone',
    version='0.1',
    license='GPLv3+',
    author='Jan Dittberner',
    author_email='jan@dittberner.info',
    description='Django app for dropzone.js integration',
    url='https://github.com/jandd/django_dropzone',
    packages=find_packages(exclude=['dropzone_demo', 'docs', 'tests']),
    install_requires=['Django>=1.9', 'Pillow>=3.0'],
    extras_require={
        'test': ['coverage'],
    }
)
