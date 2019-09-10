from flask import render_template,request,redirect,url_for
from . import main
from app.request import get_news, get_articles

@main.route('/')
def index():

    '''
    A function that returns the index page and the contents it has
    '''

    #Getting news highlights
    
    news_highlights = get_news()
    
    return render_template('index.html', highlights = news_highlights )

@main.route('/articles/<source_id>')
def articles(source_id):
    ''' ihiu '''

    articles = get_articles(source_id)

    return render_template('articles.html', articles = articles)