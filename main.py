from urllib.request import urlopen
from subprocess import call, check_output
from bs4 import BeautifulSoup
from jinja2 import Template
import re

redirect = check_output(['curl', '-s', 'http://www.urbandictionary.com/random.php']).decode("utf-8")

try:
    url = re.search(r'href="(.+)"', redirect).group(1)
except:
    print("Could not match the URL redirection.")
    raise Exception("Could not match the URL redirection.")

content = urlopen(url).read()
soup = BeautifulSoup(content, 'html.parser')

headers = soup.findAll("div", { "class" : "def-header" })
meanings = soup.findAll("div", { "class" : "meaning" })
examples = soup.findAll("div", { "class" : "example" })

term = headers[0].a.text

definition = ""
for e in meanings[0].descendants:           # if the text field contains strings
    if isinstance(e, str):                  # add them to the definition
        definition += e.strip()
    elif e.name == 'br' or e.name == 'p':   # if it contains newlines or paragraphs
        definition += '<br>'                # keep track of them too

example = ""
for e in examples[0].descendants:
    if isinstance(e, str):
        example += e.strip()
    elif e.name == 'br' or e.name == 'p':
        example += '<br>'

template = Template(open('templates/index.html', 'r').read())
print(template.render(term=term, definition=definition, example=example))
