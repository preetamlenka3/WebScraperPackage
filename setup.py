from setuptools import setup, find_packages

setup(
    name='WebScraperPackage',
    version='0.1',
    author='P charan lenka',
    author_email='preetamlenka3@gmail.com',
    description='A web scraper package for extracting quotes, images, and links from web pages.',
    long_description='This package provides a web scraper class with methods for extracting quotes, images, and links from web pages using BeautifulSoup and requests.',
    long_description_content_type='text/plain',
    url='https://github.com/preetamlenka3/WebScraperPackage.git',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
