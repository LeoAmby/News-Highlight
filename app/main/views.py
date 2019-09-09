from .request import get_news

@app.route('/')
def index():

    '''
    A function that returns the index page and the contents it has
    '''

    #Getting news highlights
    
    news_highlights = get_news('highlights')
    print(news_highlights)
    return render_template('index.html', news_highlights )