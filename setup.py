from distutils.core import setup

setup(
    name='json2xlsx',
    version='0.0.1',
    author='Messju Mohr',
    author_email='messju@lammfellpuschen.de',
    url='https://github.com/messju/json2xlsx',
    packages=['json2xlsx'],
    scripts = ['bin/json2xlsx'],
    license='MIT',
    description='A tool to convert JSON data to XLSX files',
    long_description=open('README.md').read(),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
)
