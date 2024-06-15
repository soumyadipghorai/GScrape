import sys
import os
from dotenv import main

_ = main.load_dotenv(main.find_dotenv())

# Add the parent directory to the Python path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from gscrape.scrapper import Scrapper  # Import the module from parent directory

def test_chat(url: str) -> str: 
    api_key = os.getenv("API_KEY")
    obj = Scrapper(url)
    query = input("enter query : ")
    result = obj.chat(api_key=api_key, query = query)
    return result


if __name__ == "__main__" :
    # testing existing functions 
    url = input("enter url : ") 
    print(test_chat(url))