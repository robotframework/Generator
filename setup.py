from distutils.core import setup

setup(
    name='generator',
    version='0.1.0',
    author='Mika Hänninen',
    author_email='mika.hanninen@gmail.com',
    packages=['generator'],
    scripts=['generator/generator.py'],
    include_package_data = True,
    package_data = {'generator':['*.txt']},
    download_url='https://github.com/robotframework/Generator/tarball/master',
    url='http://github.com/robotframework/Generator/',
    license='LICENSE.txt',
    description='Script which generates a test project containing test libraries, test suites and resources.',
    long_description=open('README.md').read(),
    install_requires=[],
)