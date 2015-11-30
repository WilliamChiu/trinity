from setuptools import setup

setup(
    name='trinity',
    version='0.5',
    description='Prints out assignments from trinityschoolnyc.org',
    url='https://github.com/WilliamChiu/trinity',
    author='William Chiu',
    author_email='william.chiu16@trinityschoolnyc.org',
    scripts = [
        'scripts/trinity'
    ],
    install_requires = [
        'selenium',
        'cookiejar'
    ]
)
