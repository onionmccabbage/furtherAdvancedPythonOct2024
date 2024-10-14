class NewsPublisher():
    def __init__(self):
        '''Publish a tream of events, e.g. news stories'''
        self.__subscribers = []
        self.latest_news = None
    # Observables expose 'attach' and 'detach' methods
    def attach(self, new_sub):
        self.__subscribers.append(new_sub)
    def detach(self):
        self.__subscribers.pop() # remove the most recent member
    def iter_subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]
    def notify_subs(self):
        for sub in self.__subscribers:
            sub.update()# call the update method on the subscriber
    def add_news(self, news):
        self.latest_news = news
    def get_news(self):
        return f'News just in: {self.latest_news}'