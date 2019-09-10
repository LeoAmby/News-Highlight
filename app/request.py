from app import app
import urllib.request,json
from .models import News
from config import Config
import requests

News = News.news

#api key
api_key = None
# api_key = Config.API_KEY

#Base url
base_url = None
# base_url = Config.NEWS_API_BASE_URL


def configure_request(app):
        global api_key, base_url
        api_key = app.config['API_KEY']
        base_url = app.config[]


def get_news():
    '''
    Function that gets the json response to our url request
    '''

    get_news_url = base_url + api_key

    worldNews = requests.get(get_news_url)
    news = worldNews.json()

print(news)

def process_results(news_list):
        '''
        A function that processes the movie result and transform them to a list of objects

        Args:
                news_list: these are dictionaries that have the details of the news highlights
        
        Returns:
                news_results: object of news highlights
        '''

        news_results = []
        for news_item in news_list:
                id = news_item .get('id') 
                name = news_item.get('name')
                description = news_item.get('description')
                url = news_item.get('url')
                category = news_item.get('category')
                language = news_item.get('language')
                country = news_item.get('country')





        return news_results
