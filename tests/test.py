import sys
import os

# Add the parent directory to the Python path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from gscrape.scrapper import Scrapper  # Import the module from parent directory

# testing existing functions 
url = input("enter url : ")
obj = Scrapper(url)
obj.create_markdown()