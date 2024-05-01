from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Website scrapper tool'
LONG_DESCRIPTION = 'Beautiful Soup based scrapper tool to scrape websites and convert it into markdown format. It can be used to pass data into LLM.'

# Setting up
setup(
    name="GScrape",
    version=VERSION,
    author="Soumyadip Ghorai",
    author_email="work.soumyadipghorai@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['bs4', 'requests', 'pandas', 'lxml', 'tabulate'],
    keywords=['python', 'bs4', 'beautiful soup', 'scapper', 'web scrape', 'llm'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)