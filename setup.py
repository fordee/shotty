from setuptools import setup

setup(
    name='snapshotalyzer-3000',
    version='0.1',
    author="John Forde",
    author_email="fordee@icloud.com",
    description="snapshotalyzer3000 is a tool to manage AWS EC2 instance snapshots.",
    license="MIT",
    packages=['shotty'],
    url="https://github.com/fordee/snapshotalyzer3000",
    install_requires= [
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    '''
)
