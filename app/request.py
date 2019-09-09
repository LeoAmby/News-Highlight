from app import app
import urllib.request,json
from .models import news

News = news.News

#api key
api_key = app.config['NEWS_API_KEY']

#Base url
base_url = app.config['NEWS_API_BASE_URL']

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''

    get_news_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_lists)


    return news_results
