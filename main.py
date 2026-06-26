from markdown import markdown
import os
from bs4 import BeautifulSoup


input_folder = "./input"
distribution_folder = "./dist"

def get_text_from_file(path:str):
    with open(path) as file:
        return file.read().strip()

def renden(path:str):
    res = {}
    file_text = get_text_from_file(path)
    html = markdown.markdown(file_text)
    soup = BeautifulSoup(html,"html.parser")
    res['url'] = path.split("/")[-1].split(".")[0]
    res['html'] = html
    return res


