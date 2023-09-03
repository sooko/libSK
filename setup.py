from setuptools import setup, find_packages
setup(
    name='libsk',
    version='1.2',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/sooko/libsk',
    license='MIT',
    author='Burhan',
    author_email='hansmotor89@gmail.com',
    description='Description of your project',
    install_requires=[
        'kivy',
    ],
)
