import setuptools

setuptools.setup(
    name='trinity',
    version='0.1.0',
    description='Prints out assignments from trinityschoolnyc.org',
    url='https://github.com/WilliamChiu/trinity',
    author='William Chiu',
    author_email='william.chiu16@trinityschoolnyc.org',
    scripts = [
        'scripts/trinity'
    ],
    packages=setuptools.find_packages(),
    package_data = {
        'trinity': ['settings.ini', 'settings/settings.ini']
    },
    install_requires = [
        'selenium',
        'cookiejar'
    ]
)
