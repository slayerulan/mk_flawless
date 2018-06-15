from lxml.html import fromstring
from requests_html import HTMLSession


def get_current_mirror():
    """
    Returns current available mirror of the 1xbet.com, 
    first try to redirects, if fails, try to use google
    """
    session = HTMLSession()
    url = 'http://1xstavka.ru'
    try:
        return session.get('http://1xstavka.ru').url.split('?')[0]
    except Exception as e:
        url = 'https://www.google.ru/search?&q=1xbet.com'
        try:
            r = session.get(url)
        except Exception as e:
            return "Second try, doesn't work"

        return f'https://{r.html.search("⇒ {} ⇒")[0]}'
