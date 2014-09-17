from setuptools import setup, find_packages

setup(
    name='genesis',
    description='Procedural World Generation',
    author='Nick Dumas',
    author_email='drakonik@gmail.com',
    url='https://github.com/therealfakemoot/Genesis/',
    packages=find_packages(),
    zip_safe=False,
    install_requires=['matplotlib', 'numpy', 'coverage']
)
