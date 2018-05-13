from distutils.core import setup

setup(
    name='MissionToMars',
    version='0.1.0',
    author='A. Louw',
    author_email='louwandre90@gmail.com',
    packages=['mission', 'mission.test'],
    license='LICENSE.txt',
    description='The Mars Rover Technical Challenge',
    long_description=open('README.txt').read(),
    install_requires=[
    ], )