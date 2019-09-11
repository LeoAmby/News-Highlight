
from .models import News, Articles
from config import Config
import requests


#api key
api_key = None
# api_key = Config.API_KEY

#Base url
base_url = None
# base_url = Config.NEWS_API_BASE_URL

article_url = None


def configure_request(app):
        global api_key, base_url,article_url
        api_key = app.config['API_KEY']
        base_url = app.config['NEWS_API_BASE_URL']
        article_url = app.config['NEWS_ARTICLES_URL']


def get_news():
                
        '''
        Function that gets the json response to our url request
        '''

        get_news_url = base_url + api_key

        worldNews = requests.get(get_news_url)
        news = worldNews.json()
        
        results = None
        if news['sources']:
                sources = news['sources']
                results = process_results(sources)

        return results

def process_results(sources):
        '''
        A function that processes the movie result and transform them to a list of objects

        Args:
                news_list: these are dictionaries that have the details of the news highlights
        
        Returns:
                news_results: object of news highlights
        '''

        news_results = []
        for news_item in sources:
                id = news_item .get('id') 
                name = news_item.get('name')
                description = news_item.get('description')
                url = news_item.get('url')
                category = news_item.get('category')
                language = news_item.get('language')
                country = news_item.get('country')

                s_object = News(id,name,description,url,category,language,country)
                news_results.append(s_object)
        return news_results


def get_articles(source_id):
        '''
        Function to call articles within the sources available
        '''
        print('***********************************')
        print(article_url)
        url = article_url.format(source_id,api_key) 

        article = requests.get(url)
        print(article)
        article_json = article.json()

        if article_json['articles']:
                return articles_results(article_json['articles'])
        else:
                return None


def articles_results(article_list):



        articles_items = []
        for article in article_list:
                author = article.get('author')
                title = article.get('title')
                description = article.get('description')
                image = article.get('urlToImage')
                published = article.get('publishedAt')
                url = article.get('url')

                if image:
                        obj = Articles(author,title,description,image,published,url)
                        articles_items.append(obj)

        return articles_items


