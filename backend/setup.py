from setuptools import setup

# Read the requirements.txt file
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='seo.GPT',
    version='1.0',
    description='seoGPT',
    author='Shivam Arora',
    author_email='arorashivam@protonmail.com',
    packages=['/'],
    install_requires=requirements,
)