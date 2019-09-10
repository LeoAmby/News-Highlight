from flask import render_template,request,redirect,url_for
from . import main
# from ..request import get_news,search_news
from .forms import ReviewForm
from ..models import Review
from app.request import get_news

@main.route('/')
def index():

    '''
    A function that returns the index page and the contents it has
    '''

    #Getting news highlights
    
    news_highlights = get_news()
    print(news_highlights)
    return render_template('index.html', highlights = news_highlights )