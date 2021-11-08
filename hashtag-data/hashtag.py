from bs4 import BeautifulSoup as soup 
from urllib.request import Request, urlopen


def hashtags(hash_idea):
    url = 'http://best-hashtags.com/hashtag/' + hash_idea

    try:
        req = Request(url, headers={'User-Agent' : 'Mozilla/5.0'})
        page = urlopen(req, timeout=10)
        page_html = page.read()
        page.close()
        page_soup = soup(page_html, 'html.parser')
        result = page_soup.find('div',{'class':'tag-box tag-box-v3 margin-bottom-40'})
        tags = result.decode()
        start_index = tags.find('#')
        end_index = tags.find('</p1>')
        tags = tags[start_index:end_index]
        return print(tags)
        print(end_index)
        
    except:
        print('Something went wrong While Fetching hashtags')


hash_idea = input('ENTER ONE HASH : ')  
    
hashtags(hash_idea)
