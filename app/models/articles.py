class Articles:
    """
    artcilce class defining article objects
    """

    def __init__(self,name,author,title,description,publishedAt,urlToImage,url):
      
        self.name =name
        self.author = author
        self.title = title
        self.description =description
        self.publishedAt =publishedAt
        self.urlToImage =urlToImage
        self.url =url