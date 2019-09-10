import re
from collections import Counter
from newspaper import Article

def body(url):
    output = dict()
    article = Article(url)
    article.download()
    print("fin download")
    article.parse()
    text = article.text.lower()
    words = re.split("\[a-z]",text)
    print(words)
    return output

def body1(url):
    output = dict()
    article = Article(url)
    article.download()
    article.parse()
    text = article.text.lower()
    words = re.split("\[a-z]",text)
    diccio = Counter(re.split(r'[\W\d]+',text))
    print(diccio)
    return output