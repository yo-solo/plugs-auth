import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='plugs-auth',
    package = 'plugs_auth',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    license='BSD',
    description='Reusable Authentication APP',
    long_description=README,
    url='https://bitbucket.org/solopt/plugs-auth/',
    author='Ricardo Lobo',
    author_email='ricardolobo@soloweb.pt',
    install_requires = [
        'https://bitbucket.org/solopt/plugs-core==0.1.0',
        'https://bitbucket.org/solopt/plugs-mail==0.1.0'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
