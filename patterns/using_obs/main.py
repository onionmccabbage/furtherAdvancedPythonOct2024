from news_pub import NewsPublisher
from email_sub import EmailSubscriber
from print_sub import PrintSubscriber
from media_sub import MediaSubscriber

# here we have aa global tuple
subs_t = (EmailSubscriber, PrintSubscriber, MediaSubscriber, EmailSubscriber)

def main():
    '''invoke the parts of our project'''
    news_pub = NewsPublisher()
    for subscriber in subs_t:
        subscriber(news_pub)
        # we could usse a separate loop to add news
        news_pub.add_news('News flash - its nearly time to finish for the day!!')
    # we can notify all the subscribers
    news_pub.notify_subs() # they all get notified


if __name__ == '__main__':
    main()