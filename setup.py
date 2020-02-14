from setuptools import setup, find_packages

setup(
    name='TeamPowerPackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA Team Power Python Eskom Package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Thasami601/Team_1.git',
    author='<Thasami601>',
    author_email='<thasami.soobyah@gmail.com>'
)


