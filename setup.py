from setuptools import setup

setup(
    name='trinity',
    version='0.2.0',
    description='Prints out assignments from trinityschoolnyc.org',
    url='https://github.com/WilliamChiu/trinity',
    author='William Chiu',
    author_email='william.chiu16@trinityschoolnyc.org',
    scripts = [
        'scripts/trinity'
    ],
    packages = {
        'settings'
    },
    data_files = [
        ('settings', ['settings/settings.ini'])
    ],
    install_requires = [
        'selenium',
        'cookiejar'
    ]
)
