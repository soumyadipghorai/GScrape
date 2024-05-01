import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString, Comment, ProcessingInstruction, Script, Stylesheet
import pandas as pd 
from collections import deque

class Scrapper :
    def __init__(self, site_url: str, output_type: str = 'markdown', save_file : bool = True) : 
        self.site_url = site_url 
        self.output_type = output_type 
        self.save_file = save_file
        self.HEADERS = {
            'authority': 'scrapeme.live',
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        }

        self.site_page = requests.get(self.site_url, headers = self.HEADERS)
        self.site_page_htmlcontent = self.site_page.content
        self.site_page_soup = BeautifulSoup(
            self.site_page_htmlcontent, 'lxml'
        )

    def create_markdown(self) : 
        site_body = self.site_page_soup.find('body') 
        tree_stack = deque()
        tree_stack.append(site_body)
        output = ""
        flag = True
    
        while tree_stack : 
            node = tree_stack.pop() 
            if node.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'] : 
                output += "\n"+"#"*int(node.name[-1])+ " " + node.text.strip() + '\n'

            elif node.name == 'p' : 
                output += node.text.strip() + '\n\n'
            elif node.name == 'span' : 
                if len(node.text.strip()) :
                    output += '`'+ node.text.strip() +'` ' 
            elif node.name == 'li' : 
                output += "- "
            elif node.name == 'table' :  
                extracted_table = pd.read_html(str(node))[0]
                output += '\n'+extracted_table.to_markdown() +'\n'
                flag = False 
            try :
                to_insert = []
                for child in node.children : 
                    if type(child) not in [NavigableString, Comment, ProcessingInstruction, Script, Stylesheet] and flag :
                        to_insert.append(child)
                
                to_insert = reversed(list(to_insert))
                tree_stack.extend(to_insert)
            except : 
                print("error occured --> ", node, type(node)) 
            flag = True

        if self.save_file :
            with open('example.md', 'w', encoding='utf-8') as file:
                file.write(output)

        return output
    
    def chat(self, api_key: str, query: str = "Give me a brief summary of the following text") : 
        API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
        headers = {"Authorization": f"Bearer {api_key}"}

        text = self.create_markdown()

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
            
        output = query({
            "inputs": f"{query} {text} ",
        })
    
        print(output[0]['generated_text'])