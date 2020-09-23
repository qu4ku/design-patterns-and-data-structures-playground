"""
Minimal req: 
Publisher tracks list of subscribers (adds/removes). 
Subscriber implement update method. 
"""


class Subscriber:
    def __init__(self, name):
        self.name = name 

    def update(self, article, publisher):
        print(f'{self.name} received article from publisher: {publisher.name}.')


class Publisher:
    def __init__(self, name):
        self.name = name 
        self.__subscribers = []
        self.__articles = []
    
    def add_article(self, article):
        self.__articles.append(article)
        self.notify_subscribers(article)
    
    def subscribe(self, subscriber):
        self.__subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    def notify_subscribers(self, article):
        for subscriber in self.__subscribers:
            subscriber.update(article, self)


if __name__ == '__main__':
    publisher = Publisher('BigPublisher')
    subscriber = Subscriber('Mark Suboptimal')
    publisher.subscribe(subscriber)
    publisher.add_article('Clickbait title')
