import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
# import pandas as pd
# import requests
# import time
# from pandas import json_normalize
# import json
# import io

# Function for common purposes
def url_extract (url, key, tag_class ='', type='link', bs_on=True, user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64; rv:11.0) Gecko/20100101'):
    """
    Extract article info from a news source using BeautifulSoup to pull data from HTML/XML web page.
    Args:
        url (:obj:`str`, required): url of the target news source. Eg. 'https://cafef.vn/'
        key (:obj:`str`, required): HTML tag which contains the information that you want to extract. Eg. 'h3', 'article', 'div'
        tag_class (:obj:`str`, required): The HTML class attribute specifies one or more class names for an element. Eg. 'pdate' in the tag <span class="pdate">19-11-2022 - 15:32 PM </span> on CafeF.
        type (:obj:`str`, optional): 'link' as default to extract only the article link from a news homepage. Use blank value `''` when extracting article detail on the article page.
        bs_on (:obj:`str`, optional): `True` as default. Input blank `''` when the issue is raised.
        user_agent (:obj:`str`, optional): The default value for Desktop has been provided. You can find more user agent value here: https://developers.whatismybrowser.com/useragents/explore/operating_system_name/
    """
    site_name = url.split('/')[2]
    host = 'https://' + url.split('/')[2]
    headers={'User-Agent':user_agent}
    request= urllib.request.Request(url,None,headers) 
    html = urllib.request.urlopen(request)
    bs = BeautifulSoup(html.read(), 'lxml')
    try:
        if tag_class == '':
            container = bs.find_all(key)
        else:
            container = bs.find_all(key, {'class':f'{tag_class}'})
        output, title, ext_order = extract_data(container, type, bs, bs_on)
        order = 'try'
    except:
        container = bs.select(f'{key} a[href]')
        output, title, ext_order = extract_data(container, type, bs, bs_on)
        order = 'fail'
    return output, title, host, site_name, order, ext_order

def extract_data(container, type='link', bs='', bs_on=True):
    """BeautifulSoup parser"""
    if type == 'link':
        output = [a['href'] for a in container]
        if bs != '' and bs_on == True:
            title = [a['title'] for a in container]
        else:
            title = ''
        ext_order = 'first'
    else:
        output = [time.text for time in container]
        title = bs.title.text
        ext_order = 'last'
    return output, title, ext_order

def fix_url(host, url):
    """
    Extract article info from a news source using BeautifulSoup to pull data from HTML/XML web page.
    Args:
        host (:obj:`str`, required): the host name of the news source. Eg. 'https://vneconomy.vn
        url (:obj:`str`, required): the url string of the target news source. This might not contain the host at the beginning. Eg. '/de-viet-nam-thanh-digital-hub-cua-khu-vuc-vao-nam-2030-e290.htm'
    """
    if host in url:
        return url
    else:
        if host[-1] == '/':
            host = host[:-1]
        else:
            pass
        return host + url

# vnexpress.net
## Podcast
def vne_podcast_list(url, key):
    html = urlopen(url)
    bs = BeautifulSoup(html.read(), 'lxml')
    ls = [a['href'] for a in bs.select(f'{key} a[href]')]
    return ls

def get_vne_podcast(url):
    html = urlopen(url)
    bs = BeautifulSoup(html.read(), 'lxml')
    container = bs.find_all('audio')
    for url in container:
        audio_url = url['src']
    return audio_url