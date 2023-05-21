import requests
initial_file = "/Users/viktoriatappyrova/Downloads/dataset_3378_3.txt"
url = "https://stepic.org/media/attachments/course67/3.6.3/"
answer = "./answer.txt"

def build_link(prefix:str) -> str:
    url = "https://stepic.org/media/attachments/course67/3.6.3/"
    return(url+prefix)

with open(initial_file) as init_file:
    initial_data = init_file.read().strip()
    prefix: str = requests.get(initial_data).text
    while True:
        link = build_link(prefix)
        response:str = requests.get(link).text
        if response.startswith("We"):
            with open(answer, "w") as task_answer:
                task_answer.write(response)
            print("Work is done!!!!!!")
            break
        else:
            prefix = response


import requests
import re
url_A = input()
B = input()
A = requests.get(url_A).text
pattern=r"\""
one_cross=re.split(pattern, A)
url_2=one_cross[1]
two_cross=requests.get(url_2).text
out_2=re.split(pattern,two_cross)
Q=re.split(r"\.", out_2[1])
W=re.split(r"\.",B)
if Q[1] == W[1]:
    print("Yes")
else:
    print("No")


from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

START_LINK = "https://stepik.org/media/attachments/lesson/24472/sample0.html"
END_LINK = "https://stepik.org/media/attachments/lesson/24472/sample1.html"
result = "No"

def get_soup_from_page(url: str) -> BeautifulSoup:
    request = Request(url)
    html_page = urlopen(request)
    soup = BeautifulSoup(html_page, "lxml")
    return soup

def get_links_from_soup(soup: BeautifulSoup) -> list:
    if soup is None:
        return []
    links = []
    for link in soup.findAll('a'):
        links.append(link.get('href'))

    links = [link.replace('stepic.org', 'stepik.org') for link in links]
    return links

def get_links_from_page(url):
    soup = get_soup_from_page(url)
    return get_links_from_soup(soup)

links = get_links_from_page(START_LINK)
if END_LINK not in links:
    for secondary_links in links:
        third_links = get_links_from_page(secondary_links)
        if END_LINK in third_links:
            result = "Yes"
        else:
            continue
else:
    result = "Yes"

print(result)
