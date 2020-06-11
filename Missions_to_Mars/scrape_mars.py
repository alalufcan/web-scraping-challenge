from splinter import Browser
from bs4 import BeautifulSoup
import re
import pandas as pd
from splinter.exceptions import ElementDoesNotExist

def get_nasa_mars_news(browser):
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    main = soup.find_all('div', class_='list_text')
    news_title = main.find('div', class_='content_title').get_text()
    news_p = main.find('div',class_= 'article_teaser_body').get_text()

    return {
        "news_title": news_title,
        "news_p": news_p
    }
def get_mars_image_url(browser):
    url_img = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_img)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
        
    main = soup.find('article', attrs={'class':'carousel_item'})
        
    featured_image_url  = main['style']
    featured_image_url  = re.findall(r"'(.*?)'",featured_image_url )
    featured_image_url  ='https://www.jpl.nasa.gov'+ featured_image_url [0]
    return featured_image_url

def get_mars_weather(browser):
    url_w = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url_w)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    mars_weather = soup.find_all('div', attrs={'class':'css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0'})
    url = mars_weather.find('span', class_ = 'css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0').text
    return mars_weather

def get_mars_facts(browser):
    url_facts = 'https://space-facts.com/mars/'
    tables = pd.read_html(url_facts)
    df = tables[2]
    df.columns = ['description', 'value']
    df.to_html('table.html')
    return df

def get_mars_hemispheres(browser):
    url_image = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_image)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    url_list= []
    url_full_img = "https://astrogeology.usgs.gov"
    titles = []

    for x in range (4):
        url_images = soup.find('div', class_="collapsible results").find_all('a')[x]['href']
        title = soup.find('div', class_="collapsible results").find_all('h3')[x].text
        full_url = url_full_img + url_images
        url_list.append(full_url)
        titles.append(title)

    return full_url
def scrape():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    
    mars_news = get_nasa_mars_news(browser)
    mars_image_url = get_mars_image_url(browser)
    mars_weather = get_mars_weather(browser)
    mars_facts = get_mars_facts(browser)
    mars_hemispheres = get_mars_hemispheres(browser)

    # browser.quit()
    
    mars_scraped = {
        "mars_news": mars_news,
        "mars_image_url": mars_image_url,
        "mars_weather": mars_weather,
        "mars_facts": mars_facts,
        "mars_hemispheres": mars_hemispheres
    }
    
    return mars_scraped






