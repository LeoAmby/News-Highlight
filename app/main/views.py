from . import main
from app.request import get_news
from flask import render_template

@main.route('/')
def index():

    '''
    A function that returns the index page and the contents it has
    '''

    #Getting news highlights
    
    news_highlights = get_news()
    print(news_highlights)
    return render_template('index.html', highlights = news_highlights )