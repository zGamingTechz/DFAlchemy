from setuptools import setup, find_packages

setup(
    name='dfalchemy',
    version='1.0',
    description='Generate, convert and manage DataFrames easily — perfect for devs and teachers.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Bhavya Soni',
    url='https://github.com/zGamingTechz/DFAlchemy',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'faker'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
