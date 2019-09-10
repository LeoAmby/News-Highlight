class News:
    '''
    News class to define news objects
    '''

    def __init__(self,id,name,description,url,category,language,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country


class Articles:



    def __init__(self, author, title, description,image,publishedAt,url):
        self.author = author
        self.title = title
        self.description = description
        self.image = image
        self.publishedAt = publishedAt
        self.url = url


# class Review:
#     all_reviews = []

#     def __init__(self,news_id,name,review):
#         self.news_id = news_id
#         self.name = name
#         self.review = review

    # def save_review(self):
    #     Review.all_reviews.append(self)


    # @classmethod
    # def clear_reviews(cls):
    #     Review.all_reviews.clear()


    # @classsmethod
    # def get_reviews(cls, id):

    #     response = []

    #     for review in cls.all_reviews:
    #         if review.news_id == id:
    #             response.append(review)

    #     return response
