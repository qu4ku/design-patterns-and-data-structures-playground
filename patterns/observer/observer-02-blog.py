class User:
    """
    User class will act as observer to subject.
    """
    
    def __init__(self, name):
        self.name = name

    def update(self, article, blog_writer):
        print(f'User {self.name} received notification. Article by {blog_writer.name} is added.')    


class BlogWriter:
    """
    BlogWriter class is useful to blog writer to add new article
    and manage subscribers as well.
    """
    
    def __init__(self, name):
        self.name = name
        self.__subscribers = []
        self.__articles = []
    
    def add_article(self, article):
        """
        Add new article and notify subscribers.
        """
        self.__articles.append(article)
        self.notify_subscribers(article)

    def get_articles(self):
        """
        Get articles written by {self}.
        """
        return self.__articles

    def subscribe(self, subscriber):
        """
        Add new subscriber to notify of adding an article.
        """
        self.__subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        """
        User can unsubscribe from further notifications.
        """
        return self.__subscribers.remove(subscriber)

    def notify_subscribers(self, article):
        """
        Notifying all the subscribers about the new article.
        """
        for sub in self.__subscribers:
            sub.update(article, self)


if __name__ == '__main__':
    blog_writer = BlogWriter('BigShot Writer')
    newman = User('Newman')
    oldman = User('Oldman')
    blog_writer.subscribe(newman)
    blog_writer.subscribe(oldman)
    blog_writer.add_article('New Article 1')
