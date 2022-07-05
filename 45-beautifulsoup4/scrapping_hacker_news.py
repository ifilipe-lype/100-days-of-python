from unicodedata import name
import requests
from bs4 import BeautifulSoup

yc_webiste = requests.get('https://news.ycombinator.com/news').text
soup = BeautifulSoup(yc_webiste, "html.parser");
table_news = soup.find(name="table", class_="itemlist")
articles = table_news.select(".itemlist tr")

articles_dict_by_upvote = {}

for i in range(0, len(articles) - 2, 3):
    article_tr = articles[i]
    next_article_tr = articles[i+1]

    article_link_tag = article_tr.find(name="a", class_="titlelink")
    article_title = article_link_tag.getText()
    article_link = article_link_tag.get("href")
    article_upvote = int(next_article_tr.find(name="span", class_="score").getText().split(" ")[0])

    articles_dict_by_upvote[article_upvote] = {
        "title": article_title,
        "link": article_link,
        "upvote": article_upvote
    }

most_upvoted_article_key = max(articles_dict_by_upvote.keys())
print(articles_dict_by_upvote[most_upvoted_article_key])