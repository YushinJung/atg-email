from setuptools import setup, find_packages

setup(
    name='atg-email', 
    version='0.0.0.1',
    description='sending email easily using gmail', 
    url='https://github.com/YushinJung/atg-email.git', 
    author='Yushin Jung',
    author_email='jyushin90@gmail.com',
    license='GNU General Public License v3.0',
    packages=['atg-email'], 
    install_requires=[
        'click==8.1.3'
    ]
    
)

