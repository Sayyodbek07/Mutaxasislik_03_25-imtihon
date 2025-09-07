from bs4 import BeautifulSoup
# site ga so'rov jo'natish uchun method
import requests

url = "https://daryo.uz/category/tashkent-city"
CATEGORIES = {
    "📰 Daryo.uz": "",
    "🌐 Kun.uz": "https://kun.uz/news/rss",
    "🗞 Gazeta.uz": "https://www.gazeta.uz/uz/rss/"
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}
sorov = requests.get(url, headers=headers)
data = sorov.text
news_list = []

soup = BeautifulSoup(data, "html.parser")
main_block = soup.find()
block = main_block.find("div", class_="section-pages__wrapper")
block_news = block.find_all("a", class_="featured-card")
for product in block_news:
    image = product.find("img", class_="layer")["src"]
    news_text = product.find("h2", class_="featured-card__title").get_text()
    news_list.append({
        "image": image,
        "news_text": news_text
    })






