import unittest
from app.models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Testing the functionality of the News class
    '''

    def setUp(self):
        '''
        this defined 'setup' test is made to run before every test
        '''

        self.new_news = News('our news highlight flask app')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))


if __name__ == '__main__':
    unittest.main()


